local client = {}

local socket = require("socket")
local udp = assert(socket.udp())

udp:settimeout(nil)

assert(udp:setsockname("*",0))
assert(udp:setpeername("127.0.0.1",5005))

function client.send(message)
    -- Send a TCP Message to the python Server
    print('sending data')
    udp:send(message)
end

return client