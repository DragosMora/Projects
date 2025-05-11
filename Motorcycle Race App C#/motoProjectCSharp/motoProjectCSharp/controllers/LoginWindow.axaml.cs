using Avalonia.Controls;
using motoProjectCSharp.services;

namespace motoProjectCSharp.controllers;

public partial class LoginWindow : Window
{
    private readonly IAppUserService _appUserService;
    private readonly IRaceService _raceService;
    private readonly ITeamService _teamService;

    public LoginWindow(IAppUserService appUserService, IRaceService raceService, ITeamService teamService)
    {
        InitializeComponent();
        _appUserService = appUserService;
        _raceService = raceService;
        _teamService = teamService;
    }

    private async void OnLoginClick(object sender, Avalonia.Interactivity.RoutedEventArgs e)
    {

        // Safely read input values on UI thread
        string username = UsernameTextBox.Text ?? "";
        string password = PasswordTextBox.Text ?? "";

        string? obtainedPassword = null;

        try
        {
            // Run the blocking socket call in a background thread
            obtainedPassword = await Task.Run(() =>
            {
                Console.WriteLine($"Sending login request for username: {username}");
                return _appUserService.FindPasswordByUsername(username);
            });
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error during login: {ex.Message}");
        }

        Console.WriteLine($"Received password: {obtainedPassword}");

        if (obtainedPassword == password)
        {
            Console.WriteLine("Login successful!");
            var mainWindow = new MainWindow(_appUserService, _raceService, _teamService);
            mainWindow.Show();
            this.Close();
        }
        else
        {
            Console.WriteLine("Login failed: incorrect password");
            ErrorTextBlock.IsVisible = true;
            await Task.Delay(5000);
            ErrorTextBlock.IsVisible = false;
        }
        
    }
}