#include <iostream>
#include "hidapi/hidapi.h"

using namespace std;

#define MAX_STR 255
#define CHATMIX_VENDOR_ID 0x1038
#define CHATMIX_PRODUCT_ID 0x12aa

int main() {
    // Initialize hid library
    int res = hid_init();

    hid_device *device = hid_open(CHATMIX_VENDOR_ID, CHATMIX_PRODUCT_ID, NULL);
    
    cout << device << endl;
}