# @gradio/multimodaltextbox

## 0.3.1

### Dependency updates

- @gradio/upload@0.9.1
- @gradio/client@0.18.0
- @gradio/image@0.10.1

## 0.3.0

### Highlights

#### Setting File Upload Limits ([#7909](https://github.com/gradio-app/gradio/pull/7909) [`2afca65`](https://github.com/gradio-app/gradio/commit/2afca6541912b37dc84f447c7ad4af21607d7c72))

We have added a `max_file_size` size parameter to `launch()` that limits to size of files uploaded to the server. This limit applies to each individual file. This parameter can be specified as a string or an integer (corresponding to the size in bytes).

The following code snippet sets a max file size of 5 megabytes.

```python
import gradio as gr

demo = gr.Interface(lambda x: x, "image", "image")

demo.launch(max_file_size="5mb")
# or
demo.launch(max_file_size=5 * gr.FileSize.MB)
```

![max_file_size_upload](https://github.com/gradio-app/gradio/assets/41651716/7547330c-a082-4901-a291-3f150a197e45)


#### Error states can now be cleared

When a component encounters an error, the error state shown in the UI can now be cleared by clicking on the `x` icon in the top right of the component. This applies to all types of errors, whether it's raised in the UI or the server.

![error_modal_calculator](https://github.com/gradio-app/gradio/assets/41651716/16cb071c-accd-45a6-9c18-0dea27d4bd98)

 Thanks @freddyaboulton!

### Fixes

- [#8066](https://github.com/gradio-app/gradio/pull/8066) [`624f9b9`](https://github.com/gradio-app/gradio/commit/624f9b9477f74a581a6c14119234f9efdfcda398) - make gradio dev tools a local dependency rather than bundling.  Thanks @pngwn!

### Dependency updates

- @gradio/atoms@0.7.1
- @gradio/client@0.17.0
- @gradio/image@0.10.0
- @gradio/statustracker@0.5.0
- @gradio/upload@0.9.0
- @gradio/utils@0.4.0

## 0.2.5

### Fixes

- [#8002](https://github.com/gradio-app/gradio/pull/8002) [`8903415`](https://github.com/gradio-app/gradio/commit/8903415e49b1526d31ff454b2235ea238e319c2c) - Add show_progress prop to Upload Component to bring back upload progress animation.  Thanks @freddyaboulton!

### Dependency updates

- @gradio/utils@0.3.2
- @gradio/statustracker@0.4.12
- @gradio/client@0.16.0
- @gradio/upload@0.8.5
- @gradio/atoms@0.7.0
- @gradio/icons@0.4.0
- @gradio/image@0.9.12

## 0.2.4

### Dependency updates

- @gradio/utils@0.3.1
- @gradio/atoms@0.6.2
- @gradio/statustracker@0.4.11
- @gradio/upload@0.8.4
- @gradio/image@0.9.11
- @gradio/client@0.15.1

## 0.2.3

### Features

- [#7875](https://github.com/gradio-app/gradio/pull/7875) [`e6d051d`](https://github.com/gradio-app/gradio/commit/e6d051dc8a497fdd6b4cfbd57efd4c8015b97a66) - Paste Images into MultimodalTextbox.  Thanks @abidlabs!

### Dependency updates

- @gradio/upload@0.8.3
- @gradio/client@0.15.0
- @gradio/image@0.9.10

## 0.2.2

### Fixes

- [#7848](https://github.com/gradio-app/gradio/pull/7848) [`8d7b3ca`](https://github.com/gradio-app/gradio/commit/8d7b3caebd8f95b1372f8412cadbb5862766c365) - Multimodal Textbox Loading + other fixes.  Thanks @dawoodkhan82!

### Dependency updates

- @gradio/atoms@0.6.1
- @gradio/statustracker@0.4.10
- @gradio/icons@0.3.4
- @gradio/upload@0.8.2
- @gradio/image@0.9.9

## 0.2.1

### Dependency updates

- @gradio/upload@0.8.1
- @gradio/statustracker@0.4.9
- @gradio/atoms@0.6.0
- @gradio/image@0.9.8

## 0.2.0

### Features

- [#7420](https://github.com/gradio-app/gradio/pull/7420) [`15da39f`](https://github.com/gradio-app/gradio/commit/15da39fca01d09a30cf47e7e72d7efa5052f61f8) - Multimodal Textbox (Chat Input Component).  Thanks @dawoodkhan82!

### Dependency updates

- @gradio/client@0.14.0
- @gradio/upload@0.8.0
- @gradio/image@0.9.7