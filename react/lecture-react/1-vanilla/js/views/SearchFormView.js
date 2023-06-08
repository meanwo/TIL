import Controller from "../Controller.js";
import { on, qs } from "../helpers.js";
import View from "./View.js";

const tag = "[SearchFormView]";

export default class SearchFormView extends View {
  constructor() {
    console.log(tag, "constructor");

    super(qs("#search-form-view"));

    this.inputElement = qs("[type=text]", this.element);
    this.resetElement = qs("[type=reset]", this.element);


    // false를 인자로 주면 reset button이 처음엔 보이지 않는다.
    this.showResetButton(false);
    this.bindEvents();
  }

  showResetButton(visible = true) {
    this.resetElement.style.display = visible ? "block" : "none";
  }

  bindEvents() {
    on(this.inputElement, "keyup", () => this.handleKeyup());
    this.on("submit", (event) => this.handleSubmit(event));
    this.on("reset", () => this.handleReset());
  }

  handleKeyup() {
    // {}를 사용하는 이유는 비구조화 할당을 위해서
    const { value } = this.inputElement; 
    this.showResetButton(value.length > 0);

    if (value.length <= 0) {
      this.handleReset();
    }
  }

  handleSubmit(event) {
    event.preventDefault();

    const { value } = this.inputElement;
    // custom event를 구분하기 위해 @를 붙임.
    this.emit("@submit", { value });
  }

  handleReset() {
    this.emit("@reset");
  }

  show(value = "") {
    this.inputElement.value = value;
    this.showResetButton(this.inputElement.value.length > 0);

    super.show();
  }
}

