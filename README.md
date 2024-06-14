# Frodobots SDK

This SDK allows you to set up a UDP server on port 3535 to communicate with the bot. It also generates a `test.h264` file in the root directory, where you can monitor the movements of your bot.

## Constraints
In order to use or run this SDK you need to have an account registered with Frodobots. This is meant for research purposes, reach to us here: [Frodobots Discord](https://discord.com/invite/AUegJCJwyb)

## Quick Start with Docker

1. **Clone the repository**

   git clone <repository_url>

2. **Create a .env file in the root directory**

   ```
      CHANNEL_NAME=
      RTC_TOKEN=
      RTM_TOKEN=
      USERID=
   ```

3. Fill up the environment values with the response from our SDK API endpoint (More information in the SDK Auth section).

4. **Build and run the Docker container**

   docker-compose up --build

5. **Stop the service**

   docker-compose down


## SDK Auth

In order to retrieve all .env variables with your provided API_TOKEN make a POST request to the following endpoint:

### Request

- POST `https://frodobots-web-api.onrender.com/api/v1/sdk/token`

   Body:
   ```
   {
      "bot_name": "<PROVIDED_THREE_CODE_BOT_NAME>"
   }
   ```

- Complete the Bearer token with your API token.

   ```
   Bearer <YOUR_API_TOKEN>
   ```

### Response
```
{
    "CHANNEL_NAME": "<CHANNEL_NAME>",
    "RTC_TOKEN": "<RTC_TOKEN>",
    "RTM_TOKEN": "<RTM_TOKEN>",
    "USERID": <USER_ID>
}
```
With the response values you can fill up the .env file in the root directory.


## Getting Started

1. The SDK will be running on port 3535. You can send commands to the bot by sending a UDP packet to this port.

2. After running this project, a `test.h264` file will be generated in the root directory. You can use this file to monitor the movements of your bot.

3. An example script using Pythong on how to communicate with the SDK has been provided in the `example` directory. However, you can write your own script in any programming language to communicate with the bot, as long as you send the correct commands to the UDP server.


## Contributions
- [Michael Cho](mailto:michael.cho@frodobots.com)
- [Santiago Pravisani](mailto:santiago.pravisani@frodobots.com)
- [Esteban Fuhrmann](mailto:esteban.fuhrmann@frodobots.com)

## Join our Discord
- [Frodobots Discord](https://discord.com/invite/AUegJCJwyb)

