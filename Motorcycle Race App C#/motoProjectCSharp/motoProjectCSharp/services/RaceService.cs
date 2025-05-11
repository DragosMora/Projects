using motoProjectCSharp.domain;
using motoProjectCSharp.repos;

namespace motoProjectCSharp.services;

public class RaceService : IRaceService
{
    private readonly RaceRepo _raceRepo;

    public RaceService(RaceRepo raceRepo)
    {
        _raceRepo = raceRepo;
    }

    public void SaveRace(Race race)
    {
        _raceRepo.Save(race);
    }

    public Race? FindById(long id)
    {
        return _raceRepo.FindById(id);
    }

    public List<Race> FindAll()
    {
        return _raceRepo.FindAll();
    }

    public void SignUpParticipant(Participant participant, long raceId, long participantTeamId)
    {
        _raceRepo.SignUpParticipant(participant, raceId, participantTeamId);
    }
}