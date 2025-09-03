 const globalSettings = { language: 'en-US' };
 const userSettings = { timezone: 'Berlin/Germany' };

 const allSettings = {...globalSettings, ...userSettings}

 const { language, timezone } = allSettings

 console.log("global Settings", language, "userSettings:", timezone );
