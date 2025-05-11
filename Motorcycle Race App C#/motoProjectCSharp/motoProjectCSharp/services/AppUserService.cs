using motoProjectCSharp.repos;

namespace motoProjectCSharp.services;

public class AppUserService : IAppUserService
{
    private readonly AppUserRepo _appUserRepo;

    public AppUserService(AppUserRepo appUserRepo)
    {
        _appUserRepo = appUserRepo;
    }
    
    public string? FindPasswordByUsername(string username)
    {
        return _appUserRepo.FindPasswordByUsername(username);
    }

}