#!/usr/bin/env python3
import os
import pyudev

def list_usb_cameras():
    context = pyudev.Context()
    cameras = []
    for device in context.list_devices(subsystem='video4linux'):
        if device.get('ID_BUS') == 'usb':
            cameras.append({
                'device_node': device.device_node,
                'product': device.get('ID_V4L_PRODUCT', 'Unknown')
            })
    return cameras

if __name__ == '__main__':
    for cam in list_usb_cameras():
        print(f"{cam['device_node']}: {cam['product']}")
