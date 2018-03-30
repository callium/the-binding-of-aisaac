-- Isaac Modding Reference Guide => https://moddingofisaac.com/docs/annotated.html

-- Register the mod
local aiMod = RegisterMod("AIMod", 1)

-- Create the client (running the game with '--luadebug' seemed to sove the issue)
local client = require("client")
Isaac.ConsoleOutput("MOD WORKING")

-- Shows that the mod is enabled and working
function aiMod:showEnabled()
    Isaac.RenderText("AI Mod Enabled", 100, 5, 255, 255, 255, 5)
end

-- Get the data to send to the NN
function aiMod:gatherData()
    -- Grab player location & enemy locations, determine if there is an enemy in each direction
    local player = Isaac.GetPlayer(0)
    local player_x = math.floor(player.Position.X)
    local player_y = math.floor(player.Position.Y)

    -- Get the enemies
    local enemies = Isaac.GetRoomEntities()

    -- [enemy above, enemy below, enemy left, enemy right, movement direction, shot direction]
    local data = {"0", "0", "0", "0", "0", "0"}

    local to_send = table.concat(data, " ")
    -- send data
    client.send(to_send)

    -- Just render player location
    local render_text = "Player X: " .. player_x .. " Player Y: " .. player_y
    Isaac.RenderText(render_text, 100, 15, 255, 255, 255, 5)
end

-- Add the callback (Tells the mod what to do)
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.showEnabled)
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.gatherData)
