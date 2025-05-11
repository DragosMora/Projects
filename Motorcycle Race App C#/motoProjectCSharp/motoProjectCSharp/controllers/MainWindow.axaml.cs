using Avalonia.Controls;
using Avalonia.Threading;
using motoProjectCSharp.services;
using motoProjectCSharp.domain;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace motoProjectCSharp.controllers;

public partial class MainWindow : Window
{
    private readonly IAppUserService _appUserService;
    private readonly IRaceService _raceService;
    private readonly ITeamService _teamService;

    private DispatcherTimer _refreshTimer;

    public MainWindow(IAppUserService appUserService, IRaceService raceService, ITeamService teamService)
    {
        InitializeComponent();
        _appUserService = appUserService;
        _raceService = raceService;
        _teamService = teamService;

        this.Opened += OnWindowOpenedAsync;
    }

    private async void OnWindowOpenedAsync(object? sender, EventArgs e)
    {
        try
        {
            await RefreshRaces();

            // Setup auto-refresh every 5 seconds
            _refreshTimer = new DispatcherTimer
            {
                Interval = TimeSpan.FromSeconds(5)
            };
            _refreshTimer.Tick += async (_, _) => await RefreshRaces();
            _refreshTimer.Start();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error initializing races: {ex.Message}");
        }
    }

    private async Task RefreshRaces()
    {
        try
        {
            var races = await Task.Run(() => _raceService.FindAll());
            ActiveRaces.ItemsSource = races;
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error refreshing races: {ex.Message}");
        }
    }

    private async void SwitchToTeamsWindow(object sender, Avalonia.Interactivity.RoutedEventArgs e)
    {
        _refreshTimer?.Stop();
        var teamsWindow = new TeamsWindow(_appUserService, _raceService, _teamService);
        teamsWindow.Show();
        this.Close();
    }

    private async void SwitchToParticipantsWindow(object sender, Avalonia.Interactivity.RoutedEventArgs e)
    {
        _refreshTimer?.Stop();
        var participantsWindow = new ParticipantsWindow(_appUserService, _raceService, _teamService);
        participantsWindow.Show();
        this.Close();
    }

    private async void SwitchToLoginWindow(object sender, Avalonia.Interactivity.RoutedEventArgs e)
    {
        _refreshTimer?.Stop();
        var loginWindow = new LoginWindow(_appUserService, _raceService, _teamService);
        loginWindow.Show();
        this.Close();
    }
}
