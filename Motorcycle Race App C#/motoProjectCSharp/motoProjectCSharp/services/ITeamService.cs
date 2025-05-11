using motoProjectCSharp.domain;

namespace motoProjectCSharp.services;

public interface ITeamService
{
    public void SaveTeam(Team team);
    public Team? FindById(long id);
    public List<Team> FindAll();
}