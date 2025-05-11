using motoProjectCSharp.domain;

namespace motoProjectCSharp.services;

public interface IRaceService
{
    public void SaveRace(Race race);
    public Race? FindById(long id);
    public List<Race> FindAll();
    public void SignUpParticipant(Participant participant, long raceId, long participantTeamId);
}