-- This is the code for the TCP Socket/Client
-- It will send data to the Python Server

local client = {}

local host, port = "127.0.0.1", 5005
local socket = require("socket")
local tcp = assert(socket.tcp())

tcp:connect(host, port)

tcp:settimeout(nil)

function client.receive()
    local data, err = tcp:receive()

    if err ~= nil then
		print("Socket Error: " .. err)
	end
	
	return data
end

function client.send(message)
    -- Send a TCP Message to the python Server
    print('sending data')
    tcp:send(message)
end

function client.close()
    tcp:close()
end

return client

-- Usage
-- local client = require("client")
-- client.send(data)