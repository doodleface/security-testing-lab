vcl 4.1;
backend default {
    .host = "cache-origin";
    .port = "8080";
}
sub vcl_recv {
    if (req.url ~ "^/private/") {
        return (hash);
    }
}
sub vcl_backend_response {
    if (bereq.url ~ "^/private/") {
        set beresp.ttl = 5m;
        set beresp.http.X-SecurityTestingLab-Cache-Fixture = "intentionally-cacheable-private-shape";
        unset beresp.http.Set-Cookie;
    }
}
