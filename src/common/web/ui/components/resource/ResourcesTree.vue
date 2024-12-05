<script setup lang="ts">
import { type TreeNode } from "primevue/treenode";
import Tree from "primevue/tree";
import { type PropType, ref, toRefs, unref, watch } from "vue";

function pathToSelectedResources(path: string): Record<string, boolean> {
    const selectedResources: Record<string, boolean> = {};
    selectedResources[path] = true;
    return selectedResources;
}

const props = defineProps({
    options: {
        type: Object as PropType<Object[]>,
        required: true
    },
    loading: {
        type: Boolean,
        default: false
    },
    loadingError: {
        type: String,
        default: ""
    }
});
const { options, loading, loadingError } = toRefs(props);
const model = defineModel<string>({ default: "" });

const isLoading = ref(loading.value);
if (isLoading.value) {
    watch(options, () => {
        isLoading.value = false;
        expandAll();
    });
}

const selectedResources = ref<Object>(pathToSelectedResources(model.value));
watch(selectedResources, (newResources) => {
    const paths = Object.keys(newResources);
    model.value = paths.length > 0 ? paths[0] : "";
});
watch(model, (newPath) => {
    selectedResources.value = pathToSelectedResources(newPath);
});

const expandedKeys = ref<Record<string, boolean>>({});
const expandAll = () => {
    for (let node of unref(options)) {
        expandNode(node as TreeNode);
    }
    expandedKeys.value = { ...expandedKeys.value };
};
const expandNode = (node: TreeNode) => {
    if (node.children && node.children.length) {
        expandedKeys.value[node.key] = true;

        for (let child of node.children) {
            expandNode(child);
        }
    }
};
</script>

<template>
    <Tree
        :value="options as TreeNode[]"
        :expanded-keys="expandedKeys"
        v-model:selection-keys="selectedResources"
        selection-mode="single"
        :loading="isLoading || !!loadingError"
        class="p-0 m-0 bg-transparent rounded"
    />
</template>

<style scoped lang="scss"></style>
