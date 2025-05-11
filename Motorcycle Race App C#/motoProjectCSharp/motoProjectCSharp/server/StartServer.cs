using System.Net;
using System.Net.Sockets;
using motoProjectCSharp.repos;
using motoProjectCSharp.services;
using motoProjectCSharp.network;
using System.Threading;
using System.Threading.Tasks;

namespace motoProjectCSharp.server;

public class StartServer
{
    private static int PORT = 55556;
    private static int MAX_CLIENTS = 10;

    public static async Task Run(string[] args)
    {
        var dbUrl = "";
        using (var reader = new StreamReader("database.properties"))
        {
            while (!reader.EndOfStream)
            {
                string line = reader.ReadLine();
                if (line.StartsWith("db.url="))  // Find the correct property
                {
                    dbUrl = line.Substring("db.url=".Length).Trim();
                    break;
                }
            }
        }

        var appUserRepo = new AppUserRepo(dbUrl);
        var raceRepo = new RaceRepo(dbUrl);
        var teamRepo = new TeamRepo(dbUrl);

        IAppUserService appUserService = new AppUserService(appUserRepo);
        IRaceService raceService = new RaceService(raceRepo);
        ITeamService teamService = new TeamService(teamRepo);

        var listener = new TcpListener(IPAddress.Any, PORT);
        var semaphore = new SemaphoreSlim(MAX_CLIENTS);
        listener.Start();
        Console.WriteLine("Listening on port " + PORT);

        while (true)
        {
            TcpClient client = await listener.AcceptTcpClientAsync(); 
            Console.WriteLine($"Connected to {client.Client.RemoteEndPoint}");
            
            await semaphore.WaitAsync();

            _ = Task.Run(async () =>
            {
                try
                {
                    // Create a JsonWorker or equivalent to process the request
                    var jsonWorker = new JsonWorker(client, appUserService, raceService, teamService);
                    await jsonWorker.Run(); // Handling client logic in a safe async manner
                }
                catch (Exception ex)
                {
                    Console.WriteLine($"Error handling client: {ex.Message}");
                }
                finally
                {
                    semaphore.Release(); // Release the semaphore once the client is done
                }
            });
        }
        
    }
}