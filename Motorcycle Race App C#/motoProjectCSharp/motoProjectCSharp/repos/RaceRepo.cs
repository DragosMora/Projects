using Microsoft.Data.Sqlite;

namespace motoProjectCSharp.repos;

using System.Collections.Generic;
using motoProjectCSharp.domain;

using System.Linq;
using log4net;


public class RaceRepo : IRaceRepo
    {
        private readonly string _url;
        private static readonly ILog Logger = LogManager.GetLogger(typeof(RaceRepo));

        public RaceRepo(string url)
        {
            _url = url;
        }

        public void Save(Race race)
        {
            string query = "INSERT INTO races (name, engine_size, date) VALUES (@name, @engine_size, @date)";
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query, conn))
                    {
                        Logger.Info($"Saving race: {race}");
                        cmd.Parameters.AddWithValue("@name", race.Name);
                        cmd.Parameters.AddWithValue("@engine_size", race.EngineSize);
                        cmd.Parameters.AddWithValue("@date", race.Date);
                        cmd.ExecuteNonQuery();
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error saving race: {e.Message}", e);
            }
        }

        public Race? FindById(long id)
        {
            string query1 = "SELECT * FROM races WHERE id = @id";
            string query2 = "SELECT * FROM races_participants WHERE race_id = @race_id";

            long raceId = 0, engineSize = 0;
            string? name = null, date = null;
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query1, conn))
                    {
                        Logger.Info($"Finding race by id: {id}");
                        //cmd.Parameters.AddWithValue("@id", id);
                        cmd.Parameters.Add("@id", SqliteType.Integer).Value = id;
                        using (var reader = cmd.ExecuteReader())
                        {
                            if (reader.Read())
                            {
                                raceId = reader.GetInt64(reader.GetOrdinal("id"));
                                name = reader.GetString(reader.GetOrdinal("name"));
                                engineSize = reader.GetInt64(reader.GetOrdinal("engine_size"));
                                date = reader.GetString(reader.GetOrdinal("date"));
                            }
                        }
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error finding race by id: {e.Message}", e);
            }

            if (raceId == 0)
            {
                Logger.Info($"Race not found: {id}");
                return null;
            }

            List<long> participantIds = new List<long>();
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query2, conn))
                    {
                        Logger.Info($"Finding participants by race id: {id}");
                        cmd.Parameters.AddWithValue("@race_id", id);
                        using (var reader = cmd.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                participantIds.Add(reader.GetInt64(reader.GetOrdinal("participant_id")));
                            }
                        }
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error finding participants by race id: {e.Message}", e);
            }

            List<Participant> participants = new List<Participant>();
            string placeholders = string.Join(",", participantIds.Select((participantId, index) => "@id" + index));
            string query3 = "SELECT * FROM participants WHERE id IN (" + placeholders + ")";
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query3, conn))
                    {
                        Logger.Info("Finding participants in list!");
                        for (int i = 0; i < participantIds.Count; i++)
                        {
                            cmd.Parameters.AddWithValue("@id" + i, participantIds[i]);
                        }
                        using (var reader = cmd.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                var participantId = reader.GetInt64(reader.GetOrdinal("id"));
                                var participantName = reader.GetString(reader.GetOrdinal("name"));
                                var participantIdNumber = reader.GetString(reader.GetOrdinal("id_number"));
                                var participantEngineSize = reader.GetInt64(reader.GetOrdinal("engine_size"));
                                participants.Add(new Participant(participantId, participantName, participantIdNumber, participantEngineSize));
                            }
                        }
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error finding participants: {e.Message}", e);
            }

            return new Race(raceId, name ?? "default", engineSize, date ?? "default", participants);
        }

        public List<Race> FindAll()
        {
            string query = "SELECT * FROM races";
            List<Race> races = new List<Race>();
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query, conn))
                    {
                        Logger.Info("Finding all races!");
                        using (var reader = cmd.ExecuteReader())
                        {
                            //Console.WriteLine(reader.HasRows);
                            while (reader.Read())
                            {
                                var raceId = reader.GetInt64(reader.GetOrdinal("id"));
                                var race = FindById(raceId);
                                if (race != null)
                                {
                                    races.Add(race);
                                }
                            }
                        }
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error finding races: {e.Message}", e);
            }
            return races;
            
        }
        //modify here from java project
        public void SignUpParticipant(Participant participant, long raceId, long participantTeamId)
        {
            //creating participant
            const string query1 = "INSERT INTO participants (name, id_number, engine_size) VALUES (@name, @id_number, @engine_size)";
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query1, conn))
                    {
                        Logger.Info($"Creating participant: {participant}");
                        cmd.Parameters.AddWithValue("@name", participant.Name);
                        cmd.Parameters.AddWithValue("@id_number", participant.IdNumber);
                        cmd.Parameters.AddWithValue("@engine_size", participant.EngineSize);
                        cmd.ExecuteNonQuery();

                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error creating participant: {e.Message}", e);
            }

            var participantId = 0L;
            const string query2 = "SELECT id FROM participants WHERE id_number = @id_number";
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query2, conn))
                    {
                        Logger.Info($"Finding participant: {participant.Id}");
                        cmd.Parameters.AddWithValue("@id_number", participant.IdNumber);
                        using (var reader = cmd.ExecuteReader())
                        {
                            while (reader.Read())
                            {
                                participantId = reader.GetInt64(reader.GetOrdinal("id"));
                            }
                        }
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error finding participant: {e.Message}", e);
            }
            
            const string query3 = "INSERT INTO races_participants (race_id, participant_id) VALUES (@race_id, @participant_id)";
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query3, conn))
                    {
                        Logger.Info($"Creating race participants: {participantId}");
                        cmd.Parameters.AddWithValue("@race_id", raceId);
                        cmd.Parameters.AddWithValue("@participant_id", participantId);
                        cmd.ExecuteNonQuery();
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error creating race participants: {e.Message}", e);
            }

            const string query4 = "INSERT INTO teams_participants (participant_id, team_id) VALUES (@participant_id, @team_id)";
            try
            {
                using (var conn = new SqliteConnection(_url))
                {
                    conn.Open();
                    using (var cmd = new SqliteCommand(query4, conn))
                    {
                        Logger.Info($"Creating team participants: {participantId}");
                        cmd.Parameters.AddWithValue("@participant_id", participantId);
                        cmd.Parameters.AddWithValue("@team_id", participantTeamId);
                        cmd.ExecuteNonQuery();
                    }
                }
            }
            catch (SqliteException e)
            {
                Logger.Error($"Error creating team participants: {e.Message}", e);
            }
            
        }
    }