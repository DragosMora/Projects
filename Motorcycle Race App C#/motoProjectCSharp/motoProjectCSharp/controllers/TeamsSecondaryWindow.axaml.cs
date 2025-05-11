using System.Security.Policy;
using Avalonia.Controls;
using Avalonia.Controls.Documents;
using Avalonia.Interactivity;
using motoProjectCSharp.services;
using motoProjectCSharp.domain;

namespace motoProjectCSharp.controllers;

public partial class TeamsSecondaryWindow : Window
{
    private readonly IAppUserService _appUserService;
    private readonly IRaceService _raceService;
    private readonly ITeamService _teamService;
    private readonly long _selectedTeamId;

    public TeamsSecondaryWindow(IAppUserService appUserService, IRaceService raceService, ITeamService teamService, long selectedId)
    {
        InitializeComponent();
        _appUserService = appUserService;
        _raceService = raceService;
        _teamService = teamService;
        _selectedTeamId = selectedId;
        InitializeView();

    }

    private async void InitializeView()
    {
        try
        {
            var team = await Task.Run(() => _teamService.FindById(_selectedTeamId));
            foreach (var teamMember in team.TeamMembers)
            {
                Console.WriteLine(teamMember);
            }
            Members.ItemsSource = team.TeamMembers;
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
    }

    private void SwitchToTeamsWindow(object sender, RoutedEventArgs e)
    {
        var teamsWindow = new TeamsWindow(_appUserService, _raceService, _teamService);
        teamsWindow.Show();
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