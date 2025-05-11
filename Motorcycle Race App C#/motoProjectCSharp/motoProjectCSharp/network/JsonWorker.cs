using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using motoProjectCSharp.domain;
using motoProjectCSharp.services;

namespace motoProjectCSharp.network
{
    public class JsonWorker
    {
        private readonly TcpClient _client;
        private readonly IAppUserService _appUserService;
        private readonly IRaceService _raceService;
        private readonly ITeamService _teamService;

        public JsonWorker(TcpClient client, IAppUserService appUserService, IRaceService raceService, ITeamService teamService)
        {
            _client = client;
            _appUserService = appUserService;
            _raceService = raceService;
            _teamService = teamService;
        }

        public async Task Run()
        {
            using NetworkStream stream = _client.GetStream();
            using StreamReader reader = new StreamReader(stream, Encoding.UTF8);
            using StreamWriter writer = new StreamWriter(stream, Encoding.UTF8) { AutoFlush = true };

            try
            {
                // Read JSON string
                string jsonRequest = await reader.ReadLineAsync();
                if (string.IsNullOrWhiteSpace(jsonRequest))
                {
                    Console.WriteLine("Empty request received.");
                    return;
                }

                Console.WriteLine("Received: " + jsonRequest);

                // Deserialize
                var request = JsonSerializer.Deserialize<Request>(jsonRequest);
                if (request == null)
                {
                    await writer.WriteLineAsync(JsonSerializer.Serialize(Response.Error("Invalid request format")));
                    return;
                }

                // Process request
                var response = ProcessRequest(request);

                // Serialize and send response
                string jsonResponse = JsonSerializer.Serialize(response, new JsonSerializerOptions { WriteIndented = false });
                await writer.WriteLineAsync(jsonResponse);
            }
            catch (Exception e)
            {
                Console.WriteLine($"Exception in JsonWorker: {e.Message}");
            }
            finally
            {
                _client.Close();
            }
        }

        private Response ProcessRequest(Request request)
        {
            string method = request.MethodName;
            Console.WriteLine($"Method: {method}");
            object[] parameters = request.Params;

            switch (method)
            {
                case "FindPasswordByUsername":
                    string username = parameters[0]?.ToString();
                    var password = _appUserService.FindPasswordByUsername(username);
                    return password != null ? Response.Ok(password) : Response.Ok(null);

                case "FindRaceById":
                    long raceId = Convert.ToInt64(parameters[0]);
                    var race = _raceService.FindById(raceId);
                    return race != null ? Response.Ok(race) : Response.Ok(null);

                case "FindAllRaces":
                    return Response.Ok(_raceService.FindAll());

                case "SignUpParticipant":
                    var participant = JsonSerializer.Deserialize<Participant>(parameters[0].ToString());

                    long raceId2 = ((JsonElement)parameters[1]).GetInt64();
                    long teamId = ((JsonElement)parameters[2]).GetInt64();

                    _raceService.SignUpParticipant(participant, raceId2, teamId);
                    return Response.Ok(participant);

                case "FindTeamById":
                    //long tId = Convert.ToInt64(parameters[0]);
                    long tId = ((JsonElement)parameters[0]).GetInt64();
                    var team = _teamService.FindById(tId);
                    return team != null ? Response.Ok(team) : Response.Ok(null);

                case "FindAllTeams":
                    return Response.Ok(_teamService.FindAll());

                default:
                    return Response.Error("Unknown method: " + method);
            }
        }
    }
}
