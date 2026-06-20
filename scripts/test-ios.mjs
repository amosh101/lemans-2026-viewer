// Playwright test for Le Mans 2026 viewer on iOS WebKit
import { webkit } from 'playwright';

(async () => {
  const browser = await webkit.launch(); // iOS WebKit
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 }, // iPhone 14 Pro size
    isMobile: true,
    hasTouch: true,
  });
  const page = await context.newPage();

  console.log('📱 Starting iOS WebKit test for Le Mans 2026 viewer');

  // Go to home page
  await page.goto('http://100.91.143.50:8083/?v=lemans1');
  await page.waitForLoadState('networkidle');
  console.log('✅ Home page loaded');

  // Screenshot home
  await page.screenshot({ path: '/tmp/lemans-home-ios.png', fullPage: true });
  console.log('📸 Home page screenshot saved');

  // Click on a car (e.g. #15 BMW)
  await page.click('a[href*="car.html?car=15"]');
  await page.waitForLoadState('networkidle');
  console.log('🚗 Navigated to car #15 detail');

  // Screenshot car detail
  await page.screenshot({ path: '/tmp/lemans-car15-ios.png', fullPage: true });
  console.log('📸 Car #15 detail screenshot saved');

  // Go back to home
  await page.goBack();
  await page.waitForLoadState('networkidle');

  // Click on Classes tab
  await page.click('a[href="./classes.html"]');
  await page.waitForLoadState('networkidle');
  console.log('📋 Navigated to classes page');

  // Screenshot classes
  await page.screenshot({ path: '/tmp/lemans-classes-ios.png', fullPage: true });
  console.log('📸 Classes page screenshot saved');

  // Click on a class tab (e.g. LMGT3)
  await page.click('button[data-class="LMGT3"]');
  await page.waitForTimeout(500); // let tab switch
  console.log('🏁 Switched to LMGT3 class');

  // Screenshot LMGT3 class
  await page.screenshot({ path: '/tmp/lemans-lmgt3-ios.png', fullPage: true });
  console.log('📸 LMGT3 class screenshot saved');

  await browser.close();
  console.log('✅ iOS WebKit test completed');
})();
