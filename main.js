





const webhookurl = 'webhookurl';
const payload = {
  content: 'text',
  username: 'username',
  avatar_url: 'https://en.wikipedia.org/wiki/File:Test-Logo.svg'
};
fetch(webhookurl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(payload)
})
  .then(response => {
    if (response.ok) {
      console.log('sent');
    } else {
      console.error('failed');
    }
  })
  .catch(error => {
    console.error('error:', error);
  });






