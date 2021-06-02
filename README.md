# Features

## Generate a layout
- What data can we pre-generate for the user?

## Save a Layout
  - How much can we save?
  - i3 we can probably start with their built in saving, but for sway we'll have to do more of it ourselves

## Load a layout
  - Gives you the correct container layout
  - Starts up the correct programs in that layout
  - Stop you from loading the same layout again?

## Configuration
  - YAML format (epic)
  - Variable Expansion
  - Enviroment Variables allowed
  - Configuration Inheritance

### Possible Layout
```YAML
inherits: base
variables:
    val: 1
    val2: 2
    name: John
    term: $TERM:alacritty
    dir: ~/sourcecode/work
layout:
    DP-1:
        @code: code -r {dir}

        terminal:
            vsplit:
                open: {term}
                stacked:
                  open: |
                   {term} -C "be rails s"
                   {term} -C "npm dev"

    DP-2:
        chat: |
           slack
           Discord
```

# Notes
- We might be able to hide things in the scratchpad workspace before placing them in the correct location
- Marks allows us to "tag" a container and then find it later
