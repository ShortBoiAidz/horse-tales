# Mossglen + Cinderdeep: free pixel-art sampler

Copyright (c) 2026 Fortress MSSP LLC
Support: hello@mail.programkiln.com

A small free taster of two paid pixel-art packs by the same seller: **Mossglen Hamlet** (above-ground fantasy village) and **Cinderdeep Delve** (dungeon and cave). It has 1 animated character, 12 props and 1 water-tile strip. It is not a tileset and has no Mossglen tiles.

## What is in this zip

14 PNG files, plus this README and `pixelsampler_LICENSE.md`.

| Item | Count | Files |
|---|---|---|
| Animated character (Mossglen) | 1: Isolde, 8 frames (idle 4 + walk 4), one 64x48 sheet of 16x24 cells | `pixelpack_char_isolde_sheet.png` |
| Props (Mossglen) | 7 | `pixelpack_prop_01_oak_barrel.png` (16x16), `pixelpack_prop_05_market_stall.png` (32x32), `pixelpack_prop_09_stone_well.png` (32x32), `pixelpack_prop_13_lantern_post.png` (16x32), `pixelpack_prop_18_scarecrow.png` (16x32), `pixelpack_prop_21_round_oak_tree.png` (32x32), `pixelpack_prop_27_straw_roof_hut.png` (32x32) |
| Props (Cinderdeep) | 5 | `pixelpack2_prop_10_treasure_chest.png` (16x16), `pixelpack2_prop_18_mine_cart.png` (32x16), `pixelpack2_prop_22_standing_torch.png` (16x32), `pixelpack2_prop_27_glowing_crystal_cluster.png` (32x32), `pixelpack2_prop_28_stone_archway.png` (32x32) |
| Water-tile strip (Cinderdeep) | 1 file, 3 cells of 16x16 (48x16) | `pixelpack2_underground_water_interior_variants.png` |

The three water cells are subtle interior variants of one water texture (they differ from each other by only a few pixels each). They are fill tiles, not an autotile set.

All art is reused unmodified from the two paid packs: every file is a byte-for-byte copy of the file of the same name in the paid pack. Nothing was recoloured, resized, re-saved or edited. The file-name prefix tells you the source: `pixelpack_` = Mossglen Hamlet, `pixelpack2_` = Cinderdeep Delve.

## Technical details

- PNG at native 1x size, RGBA. Alpha is only 0 or 255 (no semi-transparent pixels).
- Base grid 16x16. Props sit on the bottom row of their canvas. Light comes from the top left.
- Isolde: cell 16x24, pivot (8,23). Sheet 64x48 = 4 columns x 2 rows. Row 0 = idle_0..idle_3, row 1 = walk_0..walk_3. Frame n of row r is at x = 16n, y = 24r. She faces right; flip each 16x24 cell at runtime for left-facing. No left-facing file is included.
- Use nearest-neighbour scaling to keep the pixels crisp.
- **Two different palettes.** Mossglen Hamlet uses a 31-colour palette and Cinderdeep Delve a 30-colour palette. They are different palettes (they share 14 colours, mostly the neutral stone and wood tones, but each has its own greens/blues/pinks or teals/embers/violets). No palette file is included in this sampler, and the sampler does not merge or remap the two palettes. Expect the two sets to look related but not identical.

## What each paid pack adds

**Mossglen Hamlet** (16x16 village pack, version 1.0.0): 4 animated characters (Bram, Wren, Tobin, Isolde; this sampler has only Isolde), 36 props (this sampler has 7), a 64-tile terrain atlas (256x64; this sampler has none of it), a tile index, a 31-colour palette JSON and a preview sheet.
Link: https://mustafa-sec.itch.io/mossglen-hamlet-16x16-pixel-art-village-pack-characters-props-tiles

**Cinderdeep Delve** (16x16 dungeon and cave pack, version 2.0.0): 27 props (this sampler has 5), a 64-tile dungeon atlas (256x64; this sampler has none of it) plus 3 interior strips of 3 cells each (floor, wall, water; this sampler has the water strip), a 30-colour palette JSON, a tile index and previews. Cinderdeep has no characters.
Link: https://mustafa-sec.itch.io/cinderdeep-delve-16x16-pixel-art-dungeon-cave-pack-autotiles-props

We, Fortress MSSP LLC, are the seller of both paid packs and of this free sampler.

## How the art was made (AI disclosure)

- **Mossglen Hamlet files (Isolde and the 7 props):** script-authored pixel maps (Python with PIL and numpy). They are not downscaled image-generator output. During development an image generator was used only to make four reference images of the Mossglen characters, which served as colour and costume reference; no pixels were copied from them, and they are not part of any pack or of this sampler.
- **Cinderdeep Delve files (5 props and the water strip):** AI-assisted; the pixel maps were authored by AI-written code (Python/Pillow). No image-generation model output was used, and there was no external raster input.
- The build scripts are not included.

## Licence

See `pixelsampler_LICENSE.md`. In short: you may use the assets in your own commercial and non-commercial projects; you may not resell or redistribute the original files as-is, re-upload them to another store, claim you made them, or use them to train, fine-tune or evaluate machine-learning models. Credit is optional.

## Support

Questions or problems with the files: hello@mail.programkiln.com

Mossglen + Cinderdeep free sampler. Copyright (c) 2026 Fortress MSSP LLC.
