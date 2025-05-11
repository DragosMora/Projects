namespace motoProjectCSharp.repos;
using System;
using Microsoft.Data.Sqlite;
using log4net;
using log4net.Config;


public class AppUserRepo : IAppUserRepo
{
    private readonly string _url;
    private static readonly log4net.ILog Logger = log4net.LogManager.GetLogger
        (System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

    public AppUserRepo(string url)
    {
        //BasicConfigurator.Configure();
        
        _url = url;
    }

    public string? FindPasswordByUsername(string username)
    {
        string query = "SELECT password FROM users WHERE username = @username";
        try
        {
            using (var conn = new SqliteConnection(_url))
            {
                conn.Open();
                Logger.Info("Successfully connected to the database!");
                
                using (var stmt = new SqliteCommand(query, conn))
                {
                    stmt.Parameters.AddWithValue("@username", username);
                    var result = stmt.ExecuteScalar();
                    if (result != null)
                    {
                        Logger.Info("Password found!");
                        return result.ToString();
                    }
                }
            }
        }
        catch (SqliteException e)
        {
            Logger.Error($"Error connecting: {e.Message}", e);
            return null;
        }
        
        return null;
    }
}