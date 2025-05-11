using System.Net.Sockets;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text.Json;
using Avalonia.Data;
using motoProjectCSharp.network;
using motoProjectCSharp.domain;
using motoProjectCSharp.services;

namespace motoProjectCSharp.network;

public class AppUserServiceProxy : IAppUserService
    {
        private readonly string host;
        private readonly int port;

        public AppUserServiceProxy(string host, int port)
        {
            this.host = host;
            this.port = port;
        }

        public string? FindPasswordByUsername(string username)
        {
            Console.WriteLine($"[Proxy] Starting FindPasswordByUsername for: {username}");
            try
            {
                using (var client = new TcpClient(host, port))
                using (var stream = client.GetStream())
                using (var writer = new StreamWriter(stream) { AutoFlush = true })
                using (var reader = new StreamReader(stream))
                {
                    Console.WriteLine("[Proxy] Connected to server.");

                    var request = new Request("FindPasswordByUsername", new object[] { username });  // make sure method name matches server
                    var requestJson = JsonSerializer.Serialize(request);
                    Console.WriteLine("[Proxy] Sending request JSON: " + requestJson);
                    writer.WriteLine(requestJson);  // send with newline
                    writer.Flush();

                    var responseJson = reader.ReadLine();  // wait for newline
                    Console.WriteLine("[Proxy] Response JSON received: " + responseJson);

                    if (!string.IsNullOrEmpty(responseJson))
                    {
                        var response = JsonSerializer.Deserialize<Response>(responseJson);
                        if (response != null && response.Success)
                        {
                            Console.WriteLine($"[Proxy] Success. Data: {response.Data}");
                            return response.Data?.ToString();
                        }
                    }

                    Console.WriteLine("[Proxy] Response was null or unsuccessful.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[Proxy] Exception: {ex.Message}");
            }

            return null;
        }

    }