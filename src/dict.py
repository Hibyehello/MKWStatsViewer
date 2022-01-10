import src.core as core

stats = core.ParseParam()
kart_param = "./param/kartParam.bin"
driver_param = "./param/driverParam.bin"
vehicle_ids = stats.parse_driver_and_kart(kart_param)
character_ids = stats.parse_driver_and_kart(driver_param)

vehicle = [vehicle_ids[0x0], vehicle_ids[0x3], vehicle_ids[0x6], vehicle_ids[0x9], vehicle_ids[0xC], vehicle_ids[0xF],
           vehicle_ids[0x12], vehicle_ids[0x15], vehicle_ids[0x18], vehicle_ids[0x1B], vehicle_ids[0x1E],
           vehicle_ids[0x21], vehicle_ids[0x1], vehicle_ids[0x4], vehicle_ids[0x7], vehicle_ids[0xA], vehicle_ids[0xD],
           vehicle_ids[0x10], vehicle_ids[0x13], vehicle_ids[0x16], vehicle_ids[0x19], vehicle_ids[0x1C],
           vehicle_ids[0x1F], vehicle_ids[0x22], vehicle_ids[0x2], vehicle_ids[0x5], vehicle_ids[0x8], vehicle_ids[0xB],
           vehicle_ids[0xE], vehicle_ids[0x11], vehicle_ids[0x14], vehicle_ids[0x17], vehicle_ids[0x1A],
           vehicle_ids[0x1D], vehicle_ids[0x20], vehicle_ids[0x23]]

character = [character_ids[0x6], character_ids[0xC], character_ids[0x1], character_ids[0x4], character_ids[0x8],
             character_ids[0xD], character_ids[0xE], character_ids[0x5], character_ids[0x17], character_ids[0x0],
             character_ids[0x7], character_ids[0x10], character_ids[0xF], character_ids[0xA], character_ids[0x11],
             character_ids[0x12], character_ids[0x14], character_ids[0x18], character_ids[0xB], character_ids[0x2],
             character_ids[0x9], character_ids[0x3], character_ids[0x13], character_ids[0x17], character_ids[0x16],
             character_ids[0x15], character_ids[0x19]]
