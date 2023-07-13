import usb.core
import usb.util

id = 0x1038
device = usb.core.find(idVendor=id)
device.reset()
for cfg in device:
    for i in range(cfg.bNumInterfaces):
        if device.is_kernel_driver_active(i):
            device.detach_kernel_driver(i)

device.set_configuration()



cfg = device.get_active_configuration()
intf = cfg[(5, 0)]
usb.util.claim_interface(device, intf)
ep = usb.util.find_descriptor(intf)
print(intf)
print(ep)
print(device.read(ep.bEndpointAddress, ep.wMaxPacketSize))
