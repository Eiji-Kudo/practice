const { App } = require('@slack/bolt');
require('dotenv').config();

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  appToken: process.env.SLACK_APP_TOKEN,
  socketMode: true,
});

async function getDmChannelId(userId) {
  try {
    const result = await app.client.conversations.open({
      users: userId,
    });

    return result.channel.id;
  } catch (error) {
    console.error('Error opening DM channel:', error);
    return null;
  }
}

app.message('dm', async ({ message, client }) => {
  try {
    const channelId = await getDmChannelId(message.user);

    if (channelId) {
      await client.chat.postMessage({
        channel: channelId,
        text: 'これはDMです！',
      });
    }
  } catch (error) {
    console.error('Error sending DM:', error);
  }
});

(async () => {
  await app.start();
  console.log('⚡️ Bolt app is running! ⚡️');
})();
