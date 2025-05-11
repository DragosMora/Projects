using Avalonia.Controls;
using Avalonia.Interactivity;
using Avalonia.Threading;
using motoProjectCSharp.services;
using motoProjectCSharp.domain;

namespace motoProjectCSharp.controllers;

public partial class ParticipantsWindow : Window
{
    private readonly IAppUserService _appUserService;
    private readonly IRaceService _raceService;
    private readonly ITeamService _teamService;

    public ParticipantsWindow(IAppUserService appUserService, IRaceService raceService, ITeamService teamService)
    {
        InitializeComponent();
        _appUserService = appUserService;
        _raceService = raceService;
        _teamService = teamService;
    }

    private async void SignUp(Object sender, RoutedEventArgs e)
    {
        
        try
        {
            string participantName = "";
            string participantIdNumber = "";
            string engineSizeText = "";
            string raceIdText = "";
            string participantTeamIdText = "";

            // Access UI elements on the UI thread
            Dispatcher.UIThread.Invoke(() =>
            {
                participantName = ParticipantName.Text;
                participantIdNumber = ParticipantIdNumber.Text;
                engineSizeText = EngineSize.Text;
                raceIdText = RaceId.Text;
                participantTeamIdText = ParticipantTeamId.Text;
            });

            long usableEngineSize = long.Parse(engineSizeText);
            long raceId = long.Parse(raceIdText);
            long participantTeamId = long.Parse(participantTeamIdText);

            Participant participant = new Participant(0, participantName, participantIdNumber, usableEngineSize);

            // Execute the SignUpParticipant method on a background thread
            await Task.Run(() => _raceService.SignUpParticipant(participant, raceId, participantTeamId));

            // Optionally, provide feedback to the user on the UI thread
            Dispatcher.UIThread.InvokeAsync(() =>
            {
                Console.WriteLine($"Participant {participant.Name} signed up successfully!");
                // Update UI elements here if needed
            });
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input format for numeric fields.");
            // Optionally, display an error message to the user on the UI thread
            Dispatcher.UIThread.InvokeAsync(() => { /* Update UI error message */ });
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error signing up participant: {ex.Message}");
            // Optionally, display an error message to the user on the UI thread
            Dispatcher.UIThread.InvokeAsync(() => { /* Update UI error message */ });
        }
    }

    private void SwitchToMainWindow(Object sender, RoutedEventArgs e)
    {
        var mainWindow = new MainWindow(_appUserService, _raceService, _teamService);
        mainWindow.Show();
        this.Close();
    }

    private void SwitchToTeamsWindow(Object sender, RoutedEventArgs e)
    {
        var teamsWindow = new TeamsWindow(_appUserService, _raceService, _teamService);
        teamsWindow.Show();
        this.Close();
    }

    private void SwitchToLoginWindow(Object sender, RoutedEventArgs e)
    {
        var loginWindow = new LoginWindow(_appUserService, _raceService, _teamService);
        loginWindow.Show();
        this.Close();
    }
    
}