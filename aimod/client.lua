-- This is the code for the TCP Socket/Client
-- It will send data to the Python Server

local client = {}

local host, port = "127.0.0.1", 5005

-- This line is causing the trouble.
local socket = require("socket")
-- End trouble line

local tcp = assert(socket.tcp())

tcp:connect(host, port)

function client.send(message)
    -- Send a TCP Message to the python Server
    tcp:send(message)

    -- Try and receive a response (don't think I will be sending one)
    -- while true do
    --     local s, status, partial = tcp:receive()
    --     print(s or partial)
    --     if status == "closed" then break end
    -- end
end

function client.close()
    tcp:close()
end

return client

-- Usage
-- local client = require("client")
-- client.send(data)