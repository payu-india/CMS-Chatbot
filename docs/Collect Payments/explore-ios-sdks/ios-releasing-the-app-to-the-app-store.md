---
title: Releasing the App
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To release your app to Apple App Store:

1. In Xcode, navigate to your app’s target settings.
2. Select the Build Phases tab.
3. Add New Rund Script and use the following script in the run script’s editor area and set it to use /bin/sh. This build script will strip out the simulator slices from the framework.

```
APP_PATH="${TARGET_BUILD_DIR}/${WRAPPER_NAME}"

# This script loops through the frameworks embedded in the application and
# removes unused architectures.
find "$APP_PATH" -name '*.framework' -type d | while read -r FRAMEWORK
do
FRAMEWORK_EXECUTABLE_NAME=$(defaults read "$FRAMEWORK/Info.plist" CFBundleExecutable)
FRAMEWORK_EXECUTABLE_PATH="$FRAMEWORK/$FRAMEWORK_EXECUTABLE_NAME"
echo "Executable is $FRAMEWORK_EXECUTABLE_PATH"

EXTRACTED_ARCHS=()

for ARCH in $ARCHS
do
echo "Extracting $ARCH from $FRAMEWORK_EXECUTABLE_NAME"
lipo -extract "$ARCH" "$FRAMEWORK_EXECUTABLE_PATH" -o "$FRAMEWORK_EXECUTABLE_PATH-$ARCH"
EXTRACTED_ARCHS+=("$FRAMEWORK_EXECUTABLE_PATH-$ARCH")
done

echo "Merging extracted architectures: ${ARCHS}"
lipo -o "$FRAMEWORK_EXECUTABLE_PATH-merged" -create "${EXTRACTED_ARCHS[@]}"
rm "${EXTRACTED_ARCHS[@]}"

echo "Replacing original executable with thinned version"
rm "$FRAMEWORK_EXECUTABLE_PATH"
mv "$FRAMEWORK_EXECUTABLE_PATH-merged" "$FRAMEWORK_EXECUTABLE_PATH"

done

```

The script will look through your built application’s Frameworks folder and make sure only the architectures you’re building for are present in each framework.

4. Create an archive build of the consumer project:
   1. Navigate to Product > Archive and submit it for validation.
   2. Select Window > Organizer on the menu
   3. Select the project in the Organizer.
   4. Click the Validate button and follow the on-screen instructions.\
      The app should pass validation as the simulator architectures were removed from the framework during the build process.
5. After the validation is successful, upload it to Apple App Store.

For detailed information on releasing to Apple App Store, refer to [Daniel Kennett's Blog](https://ikennd.ac/blog/2015/02/stripping-unwanted-architectures-from-dynamic-libraries-in-xcode/).
