using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => Results.Content("<h1>ASP.NET Core Vulnerable Lab</h1><p>.NET/Kestrel/Razor/MVC route and model-binding coverage</p>", "text/html"));
app.MapGet("/health", () => Results.Json(new { app_id = "aspnet-core-vulnerable-lab", status = "ok" }));
app.MapGet("/orders/{id}", (string id) => Results.Json(new { route = "orders", id }));
app.Run();
