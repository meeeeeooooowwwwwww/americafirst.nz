# americafirst.nz

Cloudflare static-assets site matching the deployment structure used for davidaruck.com.

## Local test

From this project directory:

    npx wrangler dev

Then open the local URL Wrangler prints, normally:

    http://localhost:8787

## Alternative local test without Wrangler

    cd public
    python3 -m http.server 8787

Then open:

    http://localhost:8787

## Live deployment

Live domain routes are deliberately not included yet. Add the americafirst.nz routes only after local testing is approved.

## Background video

The site is prepared for a full-screen looping background video behind the centred YouTube player.

Place the finished MP4 at:

`public/assets/video/fog-bg.mp4`

The existing `public/assets/bg.png` remains the poster/fallback image if the video cannot autoplay or is unavailable. The video must be muted for browser autoplay, and the HTML already includes `autoplay muted loop playsinline`.

