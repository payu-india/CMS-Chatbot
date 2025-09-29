---
title: Update Apple Privacy manifest files
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
As per The Apple guidelines, we released below mention version of all iOS SDKs with privacy manifest files. You just need to run `pod update `to take latest version of iOS SDK's in your root project.

<Callout icon="📘" theme="info">
  **Apple Guideline**: Refer to [Privacy manifest files | Apple Developer Documentation](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files)
</Callout>

<Callout icon="🚧" theme="warn">
  **Minimum supported iOS version** is 12. Please update it on project and podfile.
</Callout>

| SDK                                              | Version |
| :----------------------------------------------- | :------ |
| PayUIndia-PayUParams                             | 5.4.1   |
| PayUIndia-AssetLibrary                           | 3.3.3   |
| PayUIndia-Custom-Browser                         | 10.2.1  |
| PayUIndia-CardScanner                            | 1.2.1   |
| PayUIndia-CommonUI                               | 1.0.1   |
| PayUIndia-PG-SDK                                 | 10.4.2  |
| PayUIndia-NativeOtpAssist                        | 3.3.1   |
| PayUIndia-UPI                                    | 9.1.1   |
| PayUIndia-UPICore                                | 9.2.1   |
| PayUIndia-Networking                             | 4.1.1   |
| PayUIndia-Logger                                 | 4.0.1   |
| PayUIndia-CheckoutPro/ PayUIndia-CheckoutProBase | 7.6.1   |
| PayUIndia-CrashReporter                          | 3.0.1   |
| PayUIndia-Analytics                              | 3.0.1   |
| PayUIndia-NetworkReachability                    | 2.0.    |

## NSPrivacyAccessedAPITypes Detection Script

If you want to analyse what APIs used by your app or any other dependency.

Global variable for search strings that may indicate a use of "iOS required reason API"

[https://developer.apple.com/documentation/bundleresources/privacy\_manifest\_files/describing\_use\_of\_required\_reason\_api](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_use_of_required_reason_api)

You can analyse with below Script:

```
excluded_dirs=() # e.g. ("Pods" "3rdparty")
search_string=(".creationDate"
               ".creationDateKey"
               ".modificationDate"
               ".fileModificationDate" 
               ".contentModificationDateKey" 
               ".creationDateKey"
               "getattrlist(" 
               "getattrlistbulk(" 
               "fgetattrlist(" 
               "stat.st_" # see https://developer.apple.com/documentation/kernel/stat
               "fstat("
               "fstatat("
               "lstat("
               "getattrlistat("
               "systemUptime"
               "mach_absolute_time()"
               "volumeAvailableCapacityKey"
               "volumeAvailableCapacityForImportantUsageKey"
               "volumeAvailableCapacityForOpportunisticUsageKey"
               "volumeTotalCapacityKey"
               "systemFreeSize"
               "systemSize"
               "statfs("
               "statvfs("
               "fstatfs("
               "fstatvfs("
               "getattrlist("
               "fgetattrlist("
               "getattrlistat("
               "activeInputModes"
               "UserDefaults"
               "NSUserDefaults"
               "NSFileCreationDate"
               "NSFileModificationDate"
               "NSFileSystemFreeSize"
               "NSFileSystemSize"
               "NSURLContentModificationDateKey"
               "NSURLCreationDateKey"
               "NSURLVolumeAvailableCapacityForImportantUsageKey"
               "NSURLVolumeAvailableCapacityForOpportunisticUsageKey"
               "NSURLVolumeAvailableCapacityKey"
               "NSURLVolumeTotalCapacityKey"
               "AppStorage"
               )

search_in_swift_file() {
    local file="$1"

    for string in "${search_string[@]}"; do
        # Search for the string in the file and get the line numbers
        lines=$(grep -n "$string" "$file" | cut -d ":" -f 1)
        if [ -n "$lines" ]; then
            echo "Found potentially required reason API usage '$string' in '$file'"
            one_line_string=$(echo "$lines" | tr '\n' ' ')
            echo "Line numbers: $one_line_string"
        fi
    done
}

is_excluded_dir() {
    local dir_name="$1"
    for excluded_dir in "${excluded_dirs[@]}"; do
        if [ "$dir_name" == "$excluded_dir" ]; then
            return 0
        fi
    done
    return 1
}


traverse_and_search() {
    local folder="$1"

    local dir_name=$(basename "$folder")

    if is_excluded_dir "$dir_name"; then
        return
    fi

    for item in "$folder"/*; do
        if [ -d "$item" ]; then
            traverse_and_search "$item"
        elif [ -f "$item" ] && ([[ "$item" == *.swift ]] || [[ "$item" == *.m ]] || [[ "$item" == *.h ]]); then
            search_in_swift_file "$item"
        fi
    done
}

if [ -z "$1" ]; then
    echo "Usage: $0 <directory-path>"
    exit 1
fi

echo "Searching for use of required reason API"

traverse_and_search "$1"

```

To use above script first create one file named required_reason_api_scanner.sh and save the above script in it. Then go to terminal and run below command:

`sh required_reason_api_scanner.sh <path to project>`

You will get report in your terminal, if you are using any API. like:
`Found potentially required reason API usage 'UserDefaults' in '<filepath>'`
