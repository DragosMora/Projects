using motoProjectCSharp.tests;
using Avalonia;
using motoProjectCSharp.controllers;
using motoProjectCSharp.controllers.client;
using motoProjectCSharp.server;


namespace motoProjectCSharp;

public abstract class Program
{
    public static async Task Main(string[] args)
    {
        if (args.Length > 0 && args[0] == "server")
        {
            // If argument is 'server', start the server
            await StartServer.Run(args);
        }
        else
        {
            // Otherwise, start the client (default)
            await StartClient.Run(args);
        }
        
    }
}