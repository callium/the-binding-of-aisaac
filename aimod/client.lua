-- This is the code for the TCP Socket/Client
-- It will send data to the Python Server

local client = {}

is_connected = false

local host, port = "127.0.0.1", 5005
local socket = require("socket")
local tcp = assert(socket.tcp())

tcp:connect(host, port)
is_connected = true

function client.send(message)
    -- Send a TCP Message to the python Server
    tcp:send(message)
end

function client.close()
    tcp:close()
    is_connected = false
end

return client

-- Usage
-- local client = require("client")
-- client.send(data)