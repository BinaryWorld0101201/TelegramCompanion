from tg_companion.tgclient import client
from telethon import events
from tg_companion.pluginmanager import load_plugins_info
from tg_companion.plugins import load_plugins

@client.on(events.NewMessage(outgoing=True, pattern=r"\.plugin (.+)"))
async def get_plugin_info(e):
    plugin_name = e.pattern_match.group(1)
    OUTPUT = f"Plugin Info For: {plugin_name}\n\n"

    plugins = load_plugins_info()
    if plugin_name in plugins:

        dct = plugins[plugin_name]

        for k, v in dct.items():
            OUTPUT += f"\n{k} : `{v}`"

        await e.reply(OUTPUT)
    else:
        await e.edit(f"Plugin `{plugin_name}` is not installed")


@client.on(events.NewMessage(outgoing=True, pattern=r"\.plugins"))
async def get_installed_plugins(e):
    PLUGINS = sorted(load_plugins())
    OUTPUT = f"Installed Plugins:\n\n"
    for plugin in PLUGINS:
        OUTPUT += f"`\n{plugin}`"
    await e.reply(OUTPUT)
