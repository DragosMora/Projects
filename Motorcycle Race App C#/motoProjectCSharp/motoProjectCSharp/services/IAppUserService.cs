namespace motoProjectCSharp.services;

public interface IAppUserService
{
    String? FindPasswordByUsername(string username);
}