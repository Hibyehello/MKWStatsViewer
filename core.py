import json
import struct
import os


class ParseParam:
    def __init__(self):
        pass

    # Send with filepath to kartParam.bin or driverParam.bin
    # Returns a nested list in order of vehicle/character IDs
    def parse_driver_and_kart(self, param):
        vehicles = []

        with open(param, 'rb') as f:
            fileContent = f.read()
            n_bytes = fileContent[0:4]

            n = int.from_bytes(n_bytes, 'big')

            for x in range(0, n):
                params = []

                nOffset = (x * 4 * 99) + 4
                nEndOffset = ((x + 1) * 4 * 99) + 4

                section_bytes = fileContent[nOffset:nEndOffset]

                tires = int.from_bytes(section_bytes[0x00:0x04], 'big')
                params.append(tires)
                drift_type = int.from_bytes(section_bytes[0x04:0x08], 'big')
                params.append(drift_type)
                weight_class = int.from_bytes(section_bytes[0x08:0x0C], 'big')
                params.append(weight_class)

                mod_check = int.from_bytes(section_bytes[0x0C:0x0D], 'big')
                if mod_check != 0:
                    params.extend([1, 'unmodded', 'unmodded', 'unmodded'])
                else:
                    params.append(mod_check)
                    param_id = int.from_bytes(section_bytes[0x0D:0x0E], 'big')
                    if param_id < n:
                        params.append(param_id)
                    else:
                        params.append('invalid')
                    param_check = int.from_bytes(section_bytes[0x0E:0x0F], 'big')
                    if param_check == 0 or param_check == 1:
                        params.append(param_check)
                    else:
                        params.append('invalid')
                    mii_check = int.from_bytes(section_bytes[0x0F:0x10], 'big')
                    if mii_check == 0 or mii_check == 1:
                        params.append(mii_check)
                    else:
                        params.append('invalid')

                weight = self.round_float(section_bytes[0x10:0x14])
                params.append(weight)
                bump_deviation_level = self.round_float(section_bytes[0x14:0x18])
                params.append(bump_deviation_level)
                speed = self.round_float(section_bytes[0x18:0x1C])
                params.append(speed)
                turning_speed = self.round_float(section_bytes[0x1C:0x20])
                turning_speed_percentage = round(100 * turning_speed,
                                                 len(str(turning_speed)))
                params.append(turning_speed_percentage)
                tilt = self.round_float(section_bytes[0x20:0x24])
                params.append(tilt)
                normal_accel_a0 = self.round_float(section_bytes[0x24:0x28])
                params.append(normal_accel_a0)
                normal_accel_a1 = self.round_float(section_bytes[0x28:0x2C])
                params.append(normal_accel_a1)
                normal_accel_a2 = self.round_float(section_bytes[0x2C:0x30])
                params.append(normal_accel_a2)
                normal_accel_a3 = self.round_float(section_bytes[0x30:0x34])
                params.append(normal_accel_a3)
                normal_accel_t1 = self.round_float(section_bytes[0x34:0x38])
                params.append(normal_accel_t1)
                normal_accel_t2 = self.round_float(section_bytes[0x38:0x3C])
                params.append(normal_accel_t2)
                normal_accel_t3 = self.round_float(section_bytes[0x3C:0x40])
                params.append(normal_accel_t3)
                drift_accel_a0 = self.round_float(section_bytes[0x40:0x44])
                params.append(drift_accel_a0)
                drift_accel_a1 = self.round_float(section_bytes[0x44:0x48])
                params.append(drift_accel_a1)
                drift_accel_t1 = self.round_float(section_bytes[0x48:0x4C])
                params.append(drift_accel_t1)
                manual_handling = self.round_float(section_bytes[0x4C:0x50])
                params.append(manual_handling)
                auto_handling = self.round_float(section_bytes[0x50:0x54])
                params.append(auto_handling)
                handling_reactivity = self.round_float(section_bytes[0x54:0x58])
                params.append(handling_reactivity)
                manual_drift = self.round_float(section_bytes[0x58:0x5C])
                params.append(manual_drift)
                auto_drift = self.round_float(section_bytes[0x5C:0x60])
                params.append(auto_drift)
                drift_reactivity = self.round_float(section_bytes[0x60:0x64])
                params.append(drift_reactivity)
                drift_target_angle = self.round_float(section_bytes[0x64:0x68])
                params.append(drift_target_angle)
                drift_end_correction = self.round_float(section_bytes[0x68:0x6C])
                params.append(drift_end_correction)
                miniturbo = int.from_bytes(section_bytes[0x6C:0x70], 'big')
                params.append(miniturbo)

                for kcl_flag in range(0, 64):
                    kOffset = "0x70"
                    baseDecimal = kcl_flag * 4
                    hexEntry = str(hex(baseDecimal)[2:])
                    currentValue = int(kOffset[2:], 16) + int(hexEntry, 16)
                    nextValue = currentValue + 4

                    new_kcl_type = self.round_float(section_bytes[currentValue:nextValue])
                    if kcl_flag >= 32:
                        params.append(new_kcl_type)
                    else:
                        new_kcl_type_percentage = round(100 * new_kcl_type, len(str(new_kcl_type)))
                        params.append(new_kcl_type_percentage)

                item_distanceX = self.round_float(section_bytes[0x170:0x174])
                params.append(item_distanceX)
                item_distanceZ = self.round_float(section_bytes[0x174:0x178])
                params.append(item_distanceZ)
                item_distanceY = self.round_float(section_bytes[0x178:0x17C])
                params.append(item_distanceY)
                item_unknown = self.round_float(section_bytes[0x17C:0x180])
                params.append(item_unknown)
                max_normal_accel = self.round_float(section_bytes[0x180:0x184])
                params.append(max_normal_accel)
                mega_mushroom_scale = self.round_float(section_bytes[0x184:0x188])
                params.append(mega_mushroom_scale)
                tire_distance = self.round_float(section_bytes[0x188:0x18C])
                params.append(tire_distance)

                vehicles.append(params)
            
        return vehicles

    # Only use internally
    # Send with section_bytes slice, returns rounded float from slice
    def round_float(self, hexString):
        unroundedFloat = struct.unpack('>f', hexString)[0]
        floatLengthCheck = str(unroundedFloat)
        for x in range(1, len(floatLengthCheck)):
            floatToCompare = float(f"{{:10.{x}f}}".format(unroundedFloat))
            compareFloatHex = struct.pack('>f', floatToCompare)
            if compareFloatHex == hexString:
                return floatToCompare


class Save:
    def __init__(self):
        pass

    # Receives parsed parameter list, along with some metadata
    # Returns nothing, results in saved JSON file in project folder
    # TODO: add a save button or shortcut that calls this function
    # TODO: verify this even works, this commit is untested
    def save_to_json(self, params, type, index, name):
        json_content = dict()
        filepath = "./project/dev/"

        # TODO: when implementing saves, swap out 'dev' with an f-string with argument 'project_name'
        # If you're crashing, you should probably make directory ./project/dev
        if not os.path.isdir('./project/dev/vehicles'):
            os.mkdir('./project/dev/vehicles')

        if not os.path.isdir('./project/dev/characters'):
            os.mkdir('./project/dev/characters')

        json_content['params'] = self.create_savedata(params)
        json_content['metadata'] = self.create_metadata(type, index)

        # 'name' is mainwindow.driver/kartselect.currentText()
        # If spaces cause an issue later on, we can always define names in self.determine_id()
        if type == 'kart':
            filepath += f"vehicles/{name}.json"
        elif type == 'driver':
            filepath += f"characters/{name}.json"

        with open(filepath, 'w') as r:
            json.dump(json_content, r)

    # Used in save_to_json() to create a stats dictionary
    def create_savedata(self, params):
        savedata = dict()
        savedata['tires'] = params[0]
        savedata['drift_type'] = params[1]
        savedata['weight_class'] = params[2]
        savedata['weight'] = str(params[7])
        savedata['speed'] = str(params[9])
        savedata['turning_speed'] = str(params[10])

        return savedata

    # Used in save_to_json() to create a metadata dictionary
    def create_metadata(self, type, index):
        # 'type' should be a string and values should be 'kart' or 'driver'
        # 'index' is mainwindow.driver/kartselect.currentIndex()
        metadata = dict()
        metadata['type'] = type
        metadata['id'] = self.determine_id(type, index)

        return metadata

    # I can't think of a better way to do this right now
    def determine_id(self, type, index):
        vehicle_order = ["0x0", "0x3", "0x6", "0x9", "0xC", "0xF", "0x12", "0x15", "0x18", "0x1B", "0x1E", "0x21",
                         "0x1", "0x4", "0x7", "0xA", "0xD", "0x10", "0x13", "0x16", "0x19", "0x1C", "0x1F", "0x22",
                         "0x2", "0x5", "0x8", "0xB", "0xE", "0x11", "0x14", "0x17", "0x1A", "0x1D", "0x20", "0x23"]

        character_order = ["0x6", "0xC", "0x1", "0x4", "0x8", "0xD", "0xE", "0x5", "0x17", "0x0", "0x7", "0x10", "0xF",
                           "0xA", "0x11", "0x12", "0x14", "0x18", "0xB", "0x2", "0x9", "0x3", "0x13", "0x17", "0x16",
                           "0x15", "0x19"]

        if type == 'kart':
            return vehicle_order[index]
        elif type == 'driver':
            return character_order[index]
