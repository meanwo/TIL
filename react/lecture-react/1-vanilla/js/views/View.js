import { emit, on } from "../helpers.js";

const tag = "[View]";

export default class View {
  constructor(element) {
    console.log(tag, "constructor");

    if (!element) throw "no element";

    this.element = element;
    this.originalDisplay = this.element.style.display || "";

    return this;
  }

  hide() {
    this.element.style.display = "none";
    return this;
  }

  // display값을 원래 값으로 복구할 때 orginalDisplay를 할당
  show() {
    this.element.style.display = this.originalDisplay;
    return this;
  }

  // 사용자가 발생시킨 이벤트를 수신하는 메소드
  on(eventName, handler) {
    on(this.element, eventName, handler);
    return this;
  }

  emit(eventName, data) {
    emit(this.element, eventName, data);
    return this;
  }
}
