-- Isaac Modding Reference Guide => https://moddingofisaac.com/docs/annotated.html

-- Register the mod
local aiMod = RegisterMod("AIMod", 1)
local player = Isaac.GetPlayer(1)

-- Renders the mod running text at the top.
-- Will also render important data such as training inputs
function aiMod:render()
    Isaac.RenderText("AI Mod Enabled", 100, 5, 255, 255, 255, 5)
end

function aiMod:getTime()
    local time = Isaac.GetTime()
    Isaac.RenderText(time, 100, 25, 255, 255, 255, 5)
end
-- Add the callback
aiMod:AddCallback(ModCallbacks.MC_POST_RENDER, aiMod.render)
aiMod:AddCallback(ModCallbacks.MC_POST_PERFECT_UPDATE, aiMod.getTime, player)
