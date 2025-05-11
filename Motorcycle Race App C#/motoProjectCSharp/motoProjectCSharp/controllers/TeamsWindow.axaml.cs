using Avalonia.Controls;
using Avalonia.Interactivity;
using motoProjectCSharp.services;
using motoProjectCSharp.domain;

namespace motoProjectCSharp.controllers;

public partial class TeamsWindow : Window
{
    private readonly IAppUserService _appUserService;
    private readonly IRaceService _raceService;
    private readonly ITeamService _teamService;

    public TeamsWindow(IAppUserService appUserService, IRaceService raceService, ITeamService teamService)
    {
        InitializeComponent();
        _appUserService = appUserService;
        _raceService = raceService;
        _teamService = teamService;
        InitializeView();
    }

    private async void InitializeView()
    {
        try
        {
            var teams = await Task.Run(() => _teamService.FindAll());

            if (teams == null || !teams.Any())
            {
                Console.WriteLine("No teams found.");
            }
            else
            {
                foreach (var team in teams)
                {
                    Console.WriteLine($"Loaded team: {team.Name} (ID: {team.Id})");
                }
            }

            Teams.ItemsSource = teams;
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error loading teams: " + ex.Message);
        }
    }

    private void SeeMembers(object sender, RoutedEventArgs e)
    {
        if (Teams.SelectedItem is not Team team)
        {
            Console.WriteLine("No team selected.");
            return;
        }

        var teamId = team.Id;
        var teamsSecondaryWindow = new TeamsSecondaryWindow(_appUserService, _raceService, _teamService, teamId);
        teamsSecondaryWindow.Show();
        this.Close();
    }

    private void SwitchToMainWindow(object sender, RoutedEventArgs e)
    {
        var mainWindow = new MainWindow(_appUserService, _raceService, _teamService);
        mainWindow.Show();
        this.Close();
    }

    private void SwitchToParticipantsWindow(object sender, RoutedEventArgs e)
    {
        var participantsWindow = new ParticipantsWindow(_appUserService, _raceService, _teamService);
        participantsWindow.Show();
        this.Close();
    }

    private void SwitchToLoginWindow(object sender, RoutedEventArgs e)
    {
        var loginWindow = new LoginWindow(_appUserService, _raceService, _teamService);
        loginWindow.Show();
        this.Close();
    }
}
