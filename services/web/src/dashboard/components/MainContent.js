import StatsView from "./StatsView";
import LogsView from "./LogsView";
import DevicesView from "./DevicesView";

export default function MainContent(props) {
  if (props.menuIndex == 0) {
    return <StatsView />;
  } else if (props.menuIndex == 1) {
    return <DevicesView />;
  } else if (props.menuIndex == 2) {
    return <LogsView />;
  }
  return <h1>Not implemented</h1>;
}
