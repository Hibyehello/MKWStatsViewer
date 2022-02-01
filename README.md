# StatsViewer

StatsViewer is an open-source application for viewing and editing Mario Kart Wii files.

After StatsViewer is feature-complete, we'll be creating a Wiiki page for it.

Discord Server: https://discord.gg/YYKkSfWvWz

## Roadmap
- [ ] General features:
  - [ ] Project creation
    - [ ] Check for pre-existing projects
    - [ ] Create new projects in "./project/{name}"
  - [ ] Project loading
    - [ ] Search for settings.json in "./project/{name}" for project settings
    - [ ] Search for BIN files in "./project/{name}/bin" for exported game files (if none are found, default to "./param")
    - [ ] Search for JSON files in "./project/{name}/{subdirectory}" for saved changes
- [ ] Settings window:
  - [ ] Create two categories to settings window, "Appearance" and "Project"
    - [ ] Appearance settings
      - [ ] Load JSON files from "./ui/palettes" and display them in a dropdown
    - [ ] Project settings
      - [ ] Mii fix code toggle
      - [ ] Item chance playercount modifier toggle
- [ ] Main window:
  - [ ] Separate the app into two panels (should maintain consistency throughout all tabs)
    - [ ] Left panel:
      - [ ] Create framework for adding editable values, labels, and categories
    - [ ] Right panel:
      - [ ] Create framework for 2D/3D visualization
- [ ] Compare tab:
  - [ ] Create a UI with a preview of the filename and four buttons: Current Project, Default, Open Project..., and Open File...
  - [ ] Find what files they are by filesize and header, and create options to compare them
    - [ ] Export differences in txt
- [ ] File implementation:
  - [ ] Finish kartParam:
    - [ ] Implement KCL speed/rotation factors
    - [ ] Implement support for right panel depending on what box is selected
    - [ ] Implement categories that can be shown or hidden
      - General
      - Drift
      - Acceleration
      - KCL Flags
      - Unused (hidden by default)
  - [ ] Finish driverParam:
    - [ ] Remove unused parameters (only 0x010 to 0x16C are applied in-game)
  - [ ] Add support for BSPs
    - [ ] Parse file
    - [ ] Editable values on left panel
    - [ ] 3D visualization on right panel dependent on what box is selected
  - [ ] Add support for ItemSlot.bin:
    - [ ] Parse file
    - [ ] Weighted table on left panel
    - [ ] Generated percentages on right panel
  - [ ] Add support for machine_para.bin
    - [ ] Parse file
    - [ ] Sliders with numerical values on left panel
    - [ ] Display bars on right panel
    - [ ] Autogenerate button (needs kartParam.bin and driverParam.bin to work)
  - [ ] Add support for kartCameraParam.bin
    - [ ] Parse file
    - [ ] Editable values on left panel
    - [ ] 3D visualization of camera angle
  - [ ] Add support for bikePartsDispParam.bin / kartPartsDispParam.bin
    - [ ] Parse files into one list
    - [ ] Editable values on left panel
    - [ ] Unknown visualization on right panel
  - [ ] Add support for kartDriverDispParam.bin / driverDispParam.bin
    - [ ] Parse files into one list
    - [ ] Editable values on left panel
    - [ ] Unknown visualization on right panel

The roadmap is currently incomplete and is missing features, but will do for now.
