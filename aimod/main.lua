-- Isaac Modding Reference Guide => https://moddingofisaac.com/docs/annotated.html
-- I've tested using a MacOS Symlink, however I've found that you just have to copy the updated mod into the mods folder

-- Register the mod
local aiMod = RegisterMod("AIMod", 1)

-- Get the player Entity
local player = Isaac.GetPlayer(1)

function aiMod:startTCP()
    -- Start the TCP Server
    client = require("client")
    client.send("Hello, From Isaac")
end

function aiMod:render()
    -- Renders the mod running text at the top.
    -- Will also render important data such as training inputs
    Isaac.RenderText("AI Mod Enabled", 100, 5, 255, 255, 255, 5)
end

function aiMod:getTime()
    -- Get the game time, this can be used to tell elapsed time
    -- Say, if the player stays in the first room for 5 seconds
    -- the program will hold 'r' to refresh
    local time = Isaac.GetTime()

    -- Render the time to the screen (not necessary)
    -- Isaac.RenderText(time, 100, 25, 255, 255, 255, 5)
    return time
end

function aiMod:getHealth()
    -- Get total number of isaac health (not sure where this will be used)
    local heartNum = player.GetHearts()

    -- Render the number of hearts to the screen (for debugging)
    Isaac.RenderText("Hearts: " .. heartNum, 100, 25, 255, 255, 255, 5)
    return heartNum
end

function aiMod:isaacHit()
    -- Call this function once isaac is hit
end

-- Add the callback (Tells the mod what to do)
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.render)
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.startTCP)
