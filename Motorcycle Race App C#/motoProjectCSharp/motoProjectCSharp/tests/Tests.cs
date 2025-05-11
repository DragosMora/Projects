using motoProjectCSharp.domain;
using motoProjectCSharp.repos;
using NUnit.Framework;



namespace motoProjectCSharp.tests;

public class Tests
{
    private static void RunDomainTests()
    {
        var user = new AppUser(1001L, "George", "aaa12345");
        Assert.That(1001L, Is.EqualTo(user.Id));
        Assert.That("George", Is.EqualTo(user.Name));
        Assert.That("aaa12345", Is.EqualTo(user.Password));
    }

    private static void RunRepoTests()
    {
        var dbUrl = "";
        try
        {
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
        }
        catch (IOException e)
        {
            Console.WriteLine(e.Message);
        }
        
        Console.WriteLine("Current directory: " + Environment.CurrentDirectory);

        
        var userRepo = new AppUserRepo(dbUrl);
        var password = userRepo.FindPasswordByUsername("Florin") ?? throw new Exception("Password not found!");
        Console.WriteLine($"Password: {password}");
        Assert.That(password, Is.EqualTo("1234"));

    }

    [Test]
    public void RunAllTests()
    {
        RunDomainTests();
        RunRepoTests();
    }
}