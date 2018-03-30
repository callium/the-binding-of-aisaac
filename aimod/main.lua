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
    local player = Isaac.GetPlayer(0)
    local player_x = math.floor(player.Position.X)
    local player_y = math.floor(player.Position.Y)

    -- [enemy above, enemy below, enemy left, enemy right, movement direction, shot direction]
    local data = {"0", "0", "0", "0", "0", "0"}
    local enemies = Isaac.GetRoomEntities()

    -- For each enemy check the location, set the data array correctly depending on where the enemies are
    for i=1, #enemies do
        if enemies[i]:IsVulnerableEnemy() then
            local enemy_x = math.floor(enemies[i].Position.X)
            local enemy_y = math.floor(enemies[i].Position.Y)

            local render_text = "Enemy X: " .. enemy_x .. " Enemy Y: " .. enemy_y
            Isaac.RenderText(render_text, 100, 25, 255, 255, 255, 5)

            -- Enemy above or below
            local x_diff = math.abs(player_x - enemy_x)
            if x_diff <= 20 then -- Enemy above
                if player_y > enemy_y then
                    data[1] = "1"
                end
                if player_y < enemy_y then -- Enemy below
                    data[2] = "1"
                end
            end

            -- Enemy left or right
            local y_diff = math.abs(player_y - enemy_y)
            if y_diff <= 20 then
                if player_x > enemy_x then -- Enemy left
                    data[3] = "1"
                end
                if player_x < enemy_x then -- Enemy right
                    data[4] = "1"
                end
            end
        end
    end

    -- Get movement & shot direction

    local to_send = table.concat(data, " ")
    Isaac.ConsoleOutput(to_send)
    -- send data
    client.send(to_send)

    -- Just render player location
    local render_text = "Player X: " .. player_x .. " Player Y: " .. player_y
    Isaac.RenderText(render_text, 100, 15, 255, 255, 255, 5)
end

-- Add the callback (Tells the mod what to do)
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.showEnabled)
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.gatherData)