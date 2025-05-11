using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;
using motoProjectCSharp.network;
using motoProjectCSharp.repos;
using motoProjectCSharp.services;


namespace motoProjectCSharp.controllers;

public class App : Application
{
    public override void Initialize() => AvaloniaXamlLoader.Load(this);

    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
        {
            //desktop.MainWindow = new MainWindow();
            
            
            //var secondaryWindow = new SecondaryWindow();
            //secondaryWindow.Show();
            
            AppUserServiceProxy appUserServiceProxy = new AppUserServiceProxy("localhost", 55556);
            RaceServiceProxy raceServiceProxy = new RaceServiceProxy("localhost", 55556);
            TeamServiceProxy teamServiceProxy = new TeamServiceProxy("localhost", 55556);

            var loginWindow = new LoginWindow(appUserServiceProxy, raceServiceProxy, teamServiceProxy);
            loginWindow.Show();
            
        }

        base.OnFrameworkInitializationCompleted();
    }
}