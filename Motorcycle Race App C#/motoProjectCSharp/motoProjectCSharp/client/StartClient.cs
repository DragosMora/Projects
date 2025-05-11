using Avalonia;
using motoProjectCSharp.network;
using motoProjectCSharp.tests;

namespace motoProjectCSharp.controllers.client;

public class StartClient : Application
{
    private static readonly string Host = "localhost";
    private static readonly int Port = 55556;

    public static async Task Run(string[] args)
    {
        var tests = new Tests();
        tests.RunAllTests();
        
        BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);
    }
    
    public static AppBuilder BuildAvaloniaApp() =>
        AppBuilder.Configure<App>()
            .UsePlatformDetect()
            .LogToTrace();
}
