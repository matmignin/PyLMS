function setupBTTClipsWidget(uuid) {
  const clipsToShow = window.widgetAdditionalData[uuid];
  loadBTTClips(uuid, clipsToShow);
}

function updateBTTClips(uuid, clips) {
  removeElementWithID("BTTClipboardOptions");
  clips = JSON.parse(decodeBase64(clips));
  loadBTTClips(uuid, clips);
}

function loadBTTClips(uuid, clipsToShow) {
  const config = window.widgetConfig[uuid];

  const widgetContainer = document.getElementById(uuid);
  if (!widgetContainer) {
    console.error("clipboard widget container not available");
    return;
  }

  widgetContainer.style.display = "inline-flex";
  widgetContainer.style.gap = "var(--notchbar-button-gap, 2px)";
  let order = 0;
  if (clipsToShow) {
    for (const clip of clipsToShow) {
      var lastURLSegment = clip.objectIDUri.substr(
        clip.objectIDUri.lastIndexOf("/") + 1
      );
      const iconBtn = addOrUpdateButton(
        uuid + lastURLSegment + "iconBtn",
        Object.assign({}, config, {
          BTTTouchBarButtonName: clip.previewTitle,
          BTTIconData: clip.image,
          order: order,
          BTTTouchBarOnlyShowIcon: true,
          BTTTouchBarApplyCornerRadiusTo: 1,
        }),
        widgetContainer
      );
      iconBtn.onclick = ((uuid, clip) => {
        return () => {
          showDetailOptionsForBTTClip(uuid, clip);
        };
      })(uuid, clip);

      const btn = addOrUpdateButton(
        uuid + lastURLSegment,
        Object.assign({}, config, {
          BTTTouchBarButtonName: clip.previewTitle,
          order: order,
          BTTTouchBarApplyCornerRadiusTo: 2,
          BTTTouchBarFreeSpaceBeforeButton: -3,
        }),
        widgetContainer
      );
      order++;
      btn.setAttribute("data-clip-name", clip.title);
      btn.setAttribute("data-clip-uri", clip.objectIDUri);
      btn.onclick = async (e) => {
        const clipName = e.target.getAttribute("data-clip-name");
        const clipURI = e.target.getAttribute("data-clip-uri");
        callBTT("call_widget_function", {
          BTTWidgetUUID: uuid,
          BTTWidgetFunctionParam1: clipURI,
          BTTWidgetFunction: "clippingTapped:",
        });
        // TODO do something with the return value of the clip
      };
    }
  }
}

async function showDetailOptionsForBTTClip(mainUUID, clip) {
  let justClose = false;
  var lastURLSegment = clip.objectIDUri.substr(
    clip.objectIDUri.lastIndexOf("/") + 1
  );
  const clipboardOptions = document.getElementById("BTTClipboardOptions");
  if(clipboardOptions) {
  if (clipboardOptions.getAttribute("data-uuid") === mainUUID+lastURLSegment) {
    justClose = true;
  }
  removeElementWithID("BTTClipboardOptions");

}
  if (justClose === true) {
    return;
  }
  const widgetContainer = document.getElementById(mainUUID);
  if (!widgetContainer) {
    console.error("clipboard widget container not available");
    return;
  }
  const config = window.widgetConfig[mainUUID];



  for (let i = 0; i < widgetContainer.children.length; i++) {
    const child = widgetContainer.children[i];
    const plainText = addOrUpdateButton(
      mainUUID + lastURLSegment + "plainText",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Plain",

        order: i,
        BTTIconData: await retrieveSFFontIconWithName('text.justify.left'),
        BTTTouchBarFreeSpaceBeforeButton: -3,
        BTTTouchBarIconInvert: true,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
      plainText.setAttribute('data-clip-uri', clip.objectIDUri);
      plainText.setAttribute('data-clip-option', 'plainText');

    const withFormat = addOrUpdateButton(
      mainUUID + lastURLSegment + "withFormat",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "With Format",
        order: i,
        BTTTouchBarButtonCornerRadius: 0,
        BTTIconData: await retrieveSFFontIconWithName('paintbrush'),

        BTTTouchBarIconInvert: true,
        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    withFormat.setAttribute('data-clip-uri', clip.objectIDUri);
    withFormat.setAttribute('data-clip-option', 'withFormat');

    const asFile = addOrUpdateButton(
      mainUUID + lastURLSegment + "asFile",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "File",
        order: i,


        BTTIconData: await retrieveSFFontIconWithName('arrow.down.doc'),

        BTTTouchBarIconInvert: true,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    asFile.setAttribute('data-clip-uri', clip.objectIDUri);
    asFile.setAttribute('data-clip-option', 'asFile');

    const justCopy = addOrUpdateButton(
      mainUUID + lastURLSegment + "justCopy",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Copy",
        order: i,
        BTTIconData: await retrieveSFFontIconWithName('doc.on.doc'),

        BTTTouchBarIconInvert: true,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    justCopy.setAttribute('data-clip-uri', clip.objectIDUri);
    justCopy.setAttribute('data-clip-option', 'justCopy');


    const type = addOrUpdateButton(
      mainUUID + lastURLSegment + "type",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Type",
        order: i,
        BTTIconData: await retrieveSFFontIconWithName('keyboard'),

        BTTTouchBarIconInvert: true,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    type.setAttribute('data-clip-uri', clip.objectIDUri);
    type.setAttribute('data-clip-option', 'type');

    const editImage = addOrUpdateButton(
      mainUUID + lastURLSegment + "editImage",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Edit Image",
        order: i,
        BTTIconData: await retrieveSFFontIconWithName('photo'),

        BTTTouchBarIconInvert: true,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    editImage.setAttribute('data-clip-uri', clip.objectIDUri);
    editImage.setAttribute('data-clip-option', 'editImage');


    const makeFavorite = addOrUpdateButton(
      mainUUID + lastURLSegment + "makeFavorite",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Make Favorite",
        order: i,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarOnlyShowIcon: true,
        BTTIconData: await retrieveSFFontIconWithName('star'),
        BTTTouchBarIconInvert: true,

        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    makeFavorite.setAttribute('data-clip-uri', clip.objectIDUri);
    makeFavorite.setAttribute('data-clip-option', 'makeFavorite');


    const removeFavorite = addOrUpdateButton(
      mainUUID + lastURLSegment + "removeFavorite",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Remove Favorite",
        order: i,
        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarOnlyShowIcon: true,
        BTTIconData: await retrieveSFFontIconWithName('star.fill'),
        BTTTouchBarIconInvert: true,

        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    removeFavorite.setAttribute('data-clip-uri', clip.objectIDUri);
    removeFavorite.setAttribute('data-clip-option', 'removeFavorite');



    const deleteItem = addOrUpdateButton(
      mainUUID + lastURLSegment + "deleteItem",
      Object.assign({}, config, {
        BTTTouchBarButtonName: "Delete",
        order: i,
        BTTIconData: await retrieveSFFontIconWithName('trash'),
        BTTTouchBarIconInvert: true,

        BTTTouchBarButtonCornerRadius: 0,
        BTTTouchBarOnlyShowIcon: true,

        BTTTouchBarButtonColor: config.BTTTouchBarButtonHoverColor,
        BTTTouchBarButtonHoverColor: config.BTTTouchBarButtonColor,

      }),
      child,
      true
    );
    deleteItem.setAttribute('data-clip-uri', clip.objectIDUri);
    deleteItem.setAttribute('data-clip-option', 'deleteItem');


    const div = document.createElement("div");
    div.id = "BTTClipboardOptions";
    div.setAttribute("data-uuid", mainUUID+lastURLSegment);
    div.appendChild(plainText);
    div.appendChild(withFormat);
    div.appendChild(asFile);
    div.appendChild(justCopy);
    div.appendChild(type);
    div.appendChild(editImage);
    if(config.isFavorite === true) {
      div.appendChild(removeFavorite);

    } else {
      div.appendChild(makeFavorite);

    }
    div.appendChild(deleteItem);

    for(const elem of div.children) {
      elem.onclick = async (e) => {

        const clipOption = e.target.getAttribute("data-clip-option");
        const clipURI = e.target.getAttribute("data-clip-uri");
        callBTT("call_widget_function", {
          BTTWidgetUUID: mainUUID,
          BTTWidgetFunctionParam1: clipURI,
          BTTWidgetFunctionParam2: clipOption,
          BTTWidgetFunction: "clippingOptionTapped:option:",
        });
        removeElementWithID("BTTClipboardOptions");

      };
    }

    div.style.display = "inline-flex";
    div.style.minWidth = "max-content";
    div.classList.add("new-box");

    if (child.id === mainUUID + lastURLSegment + "iconBtn") {
      widgetContainer.insertBefore(div, widgetContainer.children[i + 1]);

      break;
    }
  }
}
