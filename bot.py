import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")
    
    await event.client.send_file(
        event.chat_id,
        file="https://telegra.ph/file/9f1ccd3c3c90417f3cd75.jpg"
var accessToken = "vXgDyG59Up9UVLU9xd8dHJTGYosEdQIC" //generate by below method
HTTP.post({
  url: "https://api.projectoid.site/v1/telegram/botpanel/adduser.php",
  body: {
    bot_id: bot.token.split(":")[0],
    access_token: accessToken,
    user_id: user.telegramid
  }
})
var sdone = User.getProperty("sdone")
 if (!sdone) {
  HTTP.post({
    url: "https://projectoid.site/api/Telegram/broadcast/data.php",
    body: {
      user_id: user.telegramid,
      bot: bot.name
    },
folow_redirects: true //dont change
  })
  User.setProperty("sdone", "true", "string")
}
//Api.deleteMessage({ message_id: request.message.message_id })
var fullBotUsers = Bot.getProperty("wholeUsers",[])
var already = User.getProperty("already")
if (!already) {
  fullBotUsers.push(user.telegramid)
  Bot.setProperty("wholeUsers", fullBotUsers, "json")
User.setProperty("already", user.telegramid, "text")}
var broadcast = Bot.getProperty("Broadcast") ? Bot.getProperty("Broadcast") : []

if (!broadcast.includes(user.telegramid)) {
  broadcast.push(user.telegramid)
  Bot.setProperty("Broadcast", broadcast, "json")
}
if (request.data) {
  var message_id = request.message.message_id
  var chat_id = request.message.chat.id

  Api.deleteMessage({
    chat_id: chat_id,
    message_id: message_id
  })
}

var but = [
  [
 { text: "Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ", url: "https://t.me/the_ind_coder" },
    { text: "Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url: "https://t.me/the_ind_coders" }
  ],
  [{ text: "Hᴇʟᴘ", callback_data: "/help" }],
  [{ text: "🔐 Cʟᴏsᴇ", callback_data: "/close" }]
]

Api.sendMessage({
  text:
    "<b><i>👋🏻 Hi <a href='tg://user?id=" +
    user.telegramid +
    "'>" +
    user.first_name +
    "</a>!\n\nJust send me any instagram  reels  And Pics link to download it.</i></b>",
  reply_markup: { inline_keyboard: but },
  parse_mode: "HTML"
})

Api.deleteMessage({chat_id:chat.chatid,message_id:request.message_id})
var hh = ""
  if (!User.getProperty("UserDone")) {
  User.setProperty("UserDone", true, "boolean")
  var stat = Libs.ResourcesLib.anotherChatRes("status", "global")
  stat.add(1)
  Api.sendMessage({
    chat_id: 6417243582, //admin telegram id here
    text:
      "➕ <b>New User Notification</b> ➕\n\n👤<b>User:</b> <a href='tg://user?id=" +
      user.telegramid +
      "'>" +
      user.first_name +
      "</a> " +
      hh +
      "\n\n🆔<b> User ID :</b> <code>" +
      user.telegramid +
      "</code>\n\n🌝 <b>Total User's Count: " +
      stat.value() +
      "</b>",
    parse_mode: "html",
    disable_web_page_preview: true
  })
}
  @client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
  if (request.data) {
  var message_id = request.message.message_id
  var chat_id = request.message.chat.id

  Api.deleteMessage({
    chat_id: chat_id,
    message_id: message_id
  })
}

var but = [[{text: "🏠 Home",callback_data:"/start "}]]

Api.sendMessage({text:"<b><i>Send me any Instagram reels And Pics link to download it\n\nNote : Stories link not supported!!</i></b>",parse_mode:"HTML",
disable_web_page_preview: true,
reply_markup: {inline_keyboard:but}})

  @client.on(events.NewMessage(pattern="^/owner$"))
async def owner(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs [INDIAN](https://t.me/ITZ_ADITYA_THE_KING)\n✪ ᴏғғɪᴄɪᴀʟ ᴍᴇᴍʙᴇʀ ᴏғ ʙʀᴀɴᴅᴇᴅ\n✪ ʏᴏᴜᴛᴜʙᴇ [ᴄʜᴀɴɴᴇʟ](https://t.me/THE_IND_CODERS)\n✪ ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ."

  @client.on(events.NewMessage(pattern="^/close"))
async def close(event):
    chat_id = event.chat_id
    if event.is_private:if (request.data) {
  var message_id = request.message.message_id
  var chat_id = request.message.chat.id

  Api.deleteMessage({
    chat_id: chat_id,
    message_id: message_id
  })
}

@client.on(events.NewMessage(pattern="^/broadcast"))
async def broadcast(event):
    chat_id = event.chat_id
    if event.is_private:
var response=JSON.parse(content)
if(response.status==false){
  return Bot.sendMessage(" Some Problem In Codes Please Try Again Or Ask Here :- @the_IND_CODERS! ")
  }
var media =response.data
for(let i=0;i<media.length;i++){
   Api.sendDocument({ document: media[i].url })
  Api.sendPhoto({ photo: media[i].url })
  }
  @client.on(events.NewMessage(pattern="^/success"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:if(user.telegramid == 6417243582) {
  try {
    var msg = message
    function sendFile(type, method, cap, fileid) {
      HTTP.post({
        url: "https://projectoid.site/api/Telegram/broadcast",
        headers: { "content-type": "application/json" },
        body: {
          method: method, //for forward use forwardMessage
          text: cap,
          bot_token: bot.token,
          admin: user.telegramid,
          type: type,
          bot: bot.name,
          file_id: fileid,
          from_chat_id: request.chat.id,
          message_id: request.message_id,
          caption: cap,
          parseMode: "html", //you can change it to Markdown
          disableWebPreview: true,
          protectContent: true //if you want to allow users your broadcast message change it to false
        },
        folow_redirects: true //dont change
      })
    }
    var boarding = "🖥 <b><u>Broadcast By Admin</u></b> \n\n"
    var caption = !request.caption
      ? boarding
      : boarding + "🖇 <i>Message =</i> " + request.caption

    if (request.photo[0]) {
      sendFile("photo", "sendPhoto", caption, request.photo[0].file_id)
      return
    }
    if (request.text) {
      sendFile(
        "text",
        "sendMessage",
        message,
        null
      )
      return
    }
    if (request.video) {
      sendFile("video", "sendVideo", caption, request.video.file_id)
      return
    }
    if (request.audio) {
      sendFile("audio", "sendAudio", caption, request.audio.file_id)
      return
    }
    if (request.document) {
      sendFile("document", "sendDocument", caption, request.document.file_id)
      return
    }
    if (request.animation) {
      sendFile("animation", "sendAnimation", caption, request.animation.file_id)
      return
    }
    if (request.voice) {
      sendFile("voice", "sendVoice", caption, request.voice.file_id)
      return
    }
    if (request.video_note) {
      sendFile("video_note", "sendVideo", caption, request.video_note.file_id)
      return
    }
  } catch (err) {
    Bot.sendMessage(
      err +
        "\n\n_Solution:_ *message @Privates_RoBot with error tab screen shot and wait*"
    )
  }
  return
}
Bot.sendMessage("*You are Not a Admin*")

client.on(events.NewMessage(pattern="*"))
async def *(event):
    chat_id = event.chat_id
    if event.is_private:Api.sendMessage({chat_id:user.telegramid,
  parse_mode: "HTML",
  text: "<b><i>Processing your link...</i></b>",
  reply_to_message_id: request.message_id
})

if(message.startsWith("https://www.instagram.com/")){
var apiUrl="https://instagramdownloader.apinepdev.workers.dev/?url="+message

HTTP.get({
   url:apiUrl,
   success:"/success"
   
   })


  }else{
  Bot.sendMessage("Enter A Valid Reel Url")
 }
