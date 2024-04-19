

content = """
<script lang="ts">
    import {{get_object}} from "./process_json.ts";
    import ParamTable from "../ParamTable.svelte";
    import ShortcutTable from "../ShortcutTable.svelte";
    import DemosSection from "../DemosSection.svelte";
    import FunctionsSection from "../FunctionsSection.svelte";
    import GuidesSection from "../GuidesSection.svelte";


    let obj = get_object("{}");
</script>

<!--- Title -->
# {{obj.name}}

<!--- Usage and Embedded Component -->
<div class="codeblock"><pre><code class="code language-python">{{obj.parent}}.{{obj.name}}(···)</code></pre></div>

<!--- Description -->
### Description
## {{obj.description}}

<!-- Example Usage --> 
### Example Usage
<div class="codeblock"><pre><code class="code language-python">{{obj.example}}</code></pre></div>

<!--- Initialization -->
### Initialization
<ParamTable parameters={{obj.parameters}} />

<!--- Demos -->
### Demos 
<DemosSection demos={{obj.demos}} />

<!--- Methods -->
### Methods 
<FunctionsSection fns={{obj.fns}} event_listeners={{false}} />

<!--- Guides -->
### Guides
<GuidesSection guides={{obj.guides}}/>
"""


import json

PATH = "./gradio/"

with open("../json/docs.json", "r") as j:
    data = json.load(j)


components = ["interface", "chatinterface", "tabbedinterface", "blocks"]


for component in components:
    with open(PATH + f"{component}.svx", "w+") as file:
        file.write(content.format(component))
    print(f"Created {component}.svx")