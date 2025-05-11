using motoProjectCSharp.domain;
using motoProjectCSharp.repos;

namespace motoProjectCSharp.services;

public class TeamService : ITeamService
{
    private readonly TeamRepo _teamRepo;

    public TeamService(TeamRepo teamRepo)
    {
        _teamRepo = teamRepo;
    }

    public void SaveTeam(Team team)
    {
        _teamRepo.Save(team);
    }

    public Team? FindById(long id)
    {
        return _teamRepo.FindById(id);
    }

    public List<Team> FindAll()
    {
        return _teamRepo.FindAll();
    }
}